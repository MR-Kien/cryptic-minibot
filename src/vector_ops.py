# import os
# import json
# import time
# import re
# from openai import OpenAI
# from pathlib import Path
# from dotenv import load_dotenv
# import tiktoken  # Thêm import tiktoken

# load_dotenv()

# # --- CONFIG ---
# DATA_DIR = "data"
# STATE_FILE = "state.json"
# OPENAI_MAP_FILE = "openai_map.json"
# VECTOR_STORE_NAME = "OptiSigns-Knowledge-Base"
# ASSISTANT_NAME = "OptiBot"
# SYSTEM_PROMPT = """You are OptiBot, the customer-support bot for OptiSigns.com.
# • Tone: helpful, factual, concise.
# • Only answer using the uploaded docs.
# • Max 5 bullet points; else link to the doc.
# • When citing, always extract and use up to 3 'Article URL:' values from the retrieved document content (e.g., format as [1] Article URL: https://... at the end). Do not cite file names, paths, or use automatic file citations—extract the embedded Article URLs from the doc content only."""

# # Khởi tạo Client an toàn
# def get_client():
#     api_key = os.getenv("OPENAI_API_KEY")
#     if not api_key:
#         print("OPENAI_API_KEY not found in env!")
#         return None
#     return OpenAI(api_key=api_key)

# def load_json(filepath):
#     if os.path.exists(filepath):
#         with open(filepath, 'r') as f:
#             return json.load(f)
#     return {}

# def save_json(filepath, data):
#     with open(filepath, 'w') as f:
#         json.dump(data, f, indent=2)

# def estimate_tokens(text, model="gpt-4o-mini"):
#     encoding = tiktoken.encoding_for_model(model)
#     return len(encoding.encode(text))

# def preprocess_md_with_metadata(filepath, max_subchunk_tokens=600):
#     with open(filepath, 'r', encoding='utf-8') as f:
#         content = f.read()
    
#     # Trích xuất metadata
#     title_match = re.search(r'# (.*)\n', content)
#     title = title_match.group(1) if title_match else 'Unknown Title'
    
#     url_match = re.search(r'\*\*Article URL:\*\* (.*)\n', content)
#     article_url = url_match.group(1) if url_match else ''
    
#     id_match = re.search(r'\*\*Article ID:\*\* (.*)\n', content)
#     article_id = id_match.group(1) if id_match else ''
    
#     # Trích xuất body sau ---
#     body_start = content.find('---\n\n') + 5
#     body = content[body_start:]
    
#     # Chia body thành subchunks dựa trên token
#     paragraphs = body.split('\n\n')
#     subchunks = []
#     current_subchunk = []
#     current_tokens = 0
    
#     metadata_prefix = f"# {title}\n**Article URL:** {article_url}\n**Article ID:** {article_id}\n\n"
    
#     for para in paragraphs:
#         para_tokens = estimate_tokens(para)
#         if current_tokens + para_tokens > max_subchunk_tokens and current_subchunk:
#             subchunks.append(metadata_prefix + '\n\n'.join(current_subchunk))
#             current_subchunk = [para]
#             current_tokens = para_tokens
#         else:
#             current_subchunk.append(para)
#             current_tokens += para_tokens
    
#     if current_subchunk:
#         subchunks.append(metadata_prefix + '\n\n'.join(current_subchunk))
    
#     # Option B: Lưu thành nhiều file riêng
#     preprocessed_files = []
#     base_filename = os.path.splitext(os.path.basename(filepath))[0]
#     for i, subchunk in enumerate(subchunks, 1):
#         sub_filename = f"{base_filename}-part{i}.md"
#         sub_path = os.path.join(DATA_DIR, sub_filename)
#         with open(sub_path, 'w', encoding='utf-8') as f:
#             f.write(subchunk)
#         preprocessed_files.append((sub_path, article_id))
    
#     return preprocessed_files

# def sync_vector_store():
#     client = get_client()
#     if not client: return

#     print("Starting Vector Store Sync...")
    
#     # 1. Get/Create Vector Store
#     vector_store_id = None
#     vector_stores = client.vector_stores.list()  # Đã cập nhật từ beta
#     for vs in vector_stores.data:
#         if vs.name == VECTOR_STORE_NAME:
#             vector_store_id = vs.id
#             break
    
#     if not vector_store_id:
#         vs = client.vector_stores.create(name=VECTOR_STORE_NAME)
#         vector_store_id = vs.id
#         print(f"Created new Vector Store: {vector_store_id}")
#     else:
#         print(f"Using existing Vector Store: {vector_store_id}")

#     # 2. Sync Logic
#     state = load_json(STATE_FILE)
#     openai_map = load_json(OPENAI_MAP_FILE)
    
#     files_to_upload = []
#     local_files = {f: os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR) if f.endswith('.md')}
    
#     for filename, filepath in local_files.items():
#         # Trích xuất ID từ nội dung file
#         article_id = None
#         article_url = ''  # Thêm để preprocess
#         title = ''  # Thêm để preprocess
#         try:
#             with open(filepath, 'r', encoding='utf-8') as f:
#                 content = f.read(500)
#                 match_id = re.search(r'\*\*Article ID:\*\* (\d+)', content)
#                 if match_id: article_id = match_id.group(1)
                
#                 match_url = re.search(r'\*\*Article URL:\*\* (.*)\n', content)
#                 if match_url: article_url = match_url.group(1)
                
#                 match_title = re.search(r'# (.*)\n', content)
#                 if match_title: title = match_title.group(1)
#         except: continue

#         if not article_id: continue

#         current_ts = state.get(article_id)
#         mapped = openai_map.get(article_id, {})
#         stored_fid = mapped.get("file_id")
#         last_synced = mapped.get("synced_at")

#         if stored_fid and last_synced == current_ts:
#             continue
            
#         if stored_fid:
#             try:
#                 client.files.delete(stored_fid)
#                 print(f"Deleted outdated file for art_id {article_id}")
#             except: pass

#         # Preprocess file trước upload
#         preprocessed = preprocess_md_with_metadata(filepath, max_subchunk_tokens=600)
#         for p_path, p_id in preprocessed:
#             files_to_upload.append((p_path, p_id, current_ts))

#     # 3. Batch Upload
#     if files_to_upload:
#         print(f"Uploading {len(files_to_upload)} files...")
#         file_streams = [open(f[0], "rb") for f in files_to_upload]
        
#         file_batch = client.vector_stores.file_batches.upload_and_poll(
#             vector_store_id=vector_store_id,
#             files=file_streams
#         )
        
#         for f in file_streams: f.close()
        
#         print(f"Batch Status: {file_batch.status}")
        
#         # Lấy list files để map file_id chính xác
#         vs_files = client.vector_stores.files.list(vector_store_id=vector_store_id)
#         uploaded_ids = {}  # Map filename -> file_id
#         for file in vs_files.data:
#             file_details = client.files.retrieve(file.id)
#             if hasattr(file_details, 'filename'):
#                 uploaded_ids[file_details.filename] = file.id
        
#         # Cập nhật map chính xác
#         for f_path, art_id, ts in files_to_upload:
#             filename = os.path.basename(f_path)
#             file_id = uploaded_ids.get(filename, "unknown")  # Lấy ID nếu match
#             openai_map[art_id] = {"file_id": file_id, "synced_at": ts}
        
#         save_json(OPENAI_MAP_FILE, openai_map)
        
#         # Log chunks (như gợi ý trước)
#         total_files = 0
#         total_chunks = 0
#         vs_files = client.vector_stores.files.list(vector_store_id=vector_store_id)
#         for file in vs_files.data:
#             total_files += 1
#             file_details = client.files.retrieve(file.id)
#             chunks = file_details.metadata.get('chunk_count', 1) if hasattr(file_details, 'metadata') else 1
#             total_chunks += chunks
#         print(f"Sync Summary: {total_files} files embedded, {total_chunks} total chunks")

#     # 4. Update Assistant
#     my_assistants = client.beta.assistants.list(order="desc", limit=20)
#     assistant_id = None
#     for ast in my_assistants.data:
#         if ast.name == ASSISTANT_NAME:
#             assistant_id = ast.id
#             break
    
#     if assistant_id:
#         client.beta.assistants.update(
#             assistant_id=assistant_id,
#             tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}}
#         )
#         print(f"Updated Assistant {assistant_id}")
#     else:
#         ast = client.beta.assistants.create(
#             name=ASSISTANT_NAME,
#             instructions=SYSTEM_PROMPT,
#             model="gpt-4o-mini",
#             tools=[{"type": "file_search"}],
#             tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}}
#         )
#         print(f"Created Assistant {ast.id}")
# src/vector_ops.py
import os
import json
import re
from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv
import tiktoken
from .spaces import upload_file, download_file, list_files

load_dotenv()

# --- CONFIG ---
DATA_PREFIX = "articles/"
STATE_KEY = "state.json"
OPENAI_MAP_KEY = "openai_map.json"
VECTOR_STORE_NAME = "OptiSigns-Knowledge-Base"
ASSISTANT_NAME = "OptiBot"
SYSTEM_PROMPT = """You are OptiBot, the customer-support bot for OptiSigns.com.
• Tone: helpful, factual, concise.
• Only answer using the uploaded docs.
• Max 5 bullet points; else link to the doc.
• When citing, always extract and use up to 3 'Article URL:' values from the retrieved document content (e.g., format as [1] Article URL: https://... at the end). Do not cite file names, paths, or use automatic file citations—extract the embedded Article URLs from the doc content only."""

# Khởi tạo Client an toàn
def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY not found in env!")
        return None
    return OpenAI(api_key=api_key)

def load_json_from_spaces(key):
    temp_path = f"/tmp/{os.path.basename(key)}"
    try:
        download_file(key, temp_path)
        with open(temp_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_json_to_spaces(data, key):
    temp_path = f"/tmp/{os.path.basename(key)}"
    with open(temp_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    upload_file(temp_path, key)

def estimate_tokens(text, model="gpt-4o-mini"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def preprocess_md_with_metadata(filepath, max_subchunk_tokens=600):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Trích xuất metadata
    title_match = re.search(r'# (.*)\n', content)
    title = title_match.group(1) if title_match else 'Unknown Title'
    
    url_match = re.search(r'\*\*Article URL:\*\* (.*)\n', content)
    article_url = url_match.group(1) if url_match else ''
    
    id_match = re.search(r'\*\*Article ID:\*\* (.*)\n', content)
    article_id = id_match.group(1) if id_match else ''
    
    # Trích xuất body sau ---
    body_start = content.find('---\n\n') + 5
    body = content[body_start:]
    
    # Chia body thành subchunks dựa trên token
    paragraphs = body.split('\n\n')
    subchunks = []
    current_subchunk = []
    current_tokens = 0
    
    metadata_prefix = f"# {title}\n**Article URL:** {article_url}\n**Article ID:** {article_id}\n\n"
    
    for para in paragraphs:
        para_tokens = estimate_tokens(para)
        if current_tokens + para_tokens > max_subchunk_tokens and current_subchunk:
            subchunks.append(metadata_prefix + '\n\n'.join(current_subchunk))
            current_subchunk = [para]
            current_tokens = para_tokens
        else:
            current_subchunk.append(para)
            current_tokens += para_tokens
    
    if current_subchunk:
        subchunks.append(metadata_prefix + '\n\n'.join(current_subchunk))
    
    # Option B: Lưu thành nhiều file riêng
    preprocessed_files = []
    base_filename = os.path.splitext(os.path.basename(filepath))[0]
    Path("/tmp/data").mkdir(parents=True, exist_ok=True)
    for i, subchunk in enumerate(subchunks, 1):
        sub_filename = f"{base_filename}-part{i}.md"
        sub_path = os.path.join("/tmp/data", sub_filename)
        with open(sub_path, 'w', encoding='utf-8') as f:
            f.write(subchunk)
        preprocessed_files.append((sub_path, article_id))
    
    return preprocessed_files

def sync_vector_store():
    client = get_client()
    if not client: return

    print("Starting Vector Store Sync...")
    
    # 1. Get/Create Vector Store
    vector_store_id = None
    vector_stores = client.vector_stores.list()  # Đã cập nhật từ beta
    for vs in vector_stores.data:
        if vs.name == VECTOR_STORE_NAME:
            vector_store_id = vs.id
            break
    
    if not vector_store_id:
        vs = client.vector_stores.create(name=VECTOR_STORE_NAME)
        vector_store_id = vs.id
        print(f"Created new Vector Store: {vector_store_id}")
    else:
        print(f"Using existing Vector Store: {vector_store_id}")

    # 2. Sync Logic
    state = load_json_from_spaces(STATE_KEY)
    openai_map = load_json_from_spaces(OPENAI_MAP_KEY)
    
    files_to_upload = []
    # List và download từ Spaces thay vì local dir
    keys = [k for k in list_files(prefix=DATA_PREFIX) if k.endswith('.md')]
    Path("/tmp/data").mkdir(parents=True, exist_ok=True)
    for key in keys:
        filename = os.path.basename(key)
        filepath = os.path.join("/tmp/data", filename)
        download_file(key, filepath)
        
        # Trích xuất ID từ nội dung file
        article_id = None
        article_url = ''  # Thêm để preprocess
        title = ''  # Thêm để preprocess
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read(500)
                match_id = re.search(r'\*\*Article ID:\*\* (\d+)', content)
                if match_id: article_id = match_id.group(1)
                
                match_url = re.search(r'\*\*Article URL:\*\* (.*)\n', content)
                if match_url: article_url = match_url.group(1)
                
                match_title = re.search(r'# (.*)\n', content)
                if match_title: title = match_title.group(1)
        except: continue

        if not article_id: continue

        current_ts = state.get(article_id)
        mapped = openai_map.get(article_id, {})
        stored_fid = mapped.get("file_id")
        last_synced = mapped.get("synced_at")

        if stored_fid and last_synced == current_ts:
            continue
            
        if stored_fid:
            try:
                client.files.delete(stored_fid)
                print(f"Deleted outdated file for art_id {article_id}")
            except: pass

        # Preprocess file trước upload
        preprocessed = preprocess_md_with_metadata(filepath, max_subchunk_tokens=600)
        for p_path, p_id in preprocessed:
            files_to_upload.append((p_path, p_id, current_ts))

    # 3. Batch Upload
    if files_to_upload:
        print(f"Uploading {len(files_to_upload)} files...")
        file_streams = [open(f[0], "rb") for f in files_to_upload]
        
        file_batch = client.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store_id,
            files=file_streams
        )
        
        for f in file_streams: f.close()
        
        print(f"Batch Status: {file_batch.status}")
        
        # Lấy list files để map file_id chính xác
        vs_files = client.vector_stores.files.list(vector_store_id=vector_store_id)
        uploaded_ids = {}  # Map filename -> file_id
        for file in vs_files.data:
            file_details = client.files.retrieve(file.id)
            if hasattr(file_details, 'filename'):
                uploaded_ids[file_details.filename] = file.id
        
        # Cập nhật map chính xác
        for f_path, art_id, ts in files_to_upload:
            filename = os.path.basename(f_path)
            file_id = uploaded_ids.get(filename, "unknown")  # Lấy ID nếu match
            openai_map[art_id] = {"file_id": file_id, "synced_at": ts}
        
        save_json_to_spaces(openai_map, OPENAI_MAP_KEY)
        
        # Log chunks (như gợi ý trước)
        total_files = 0
        total_chunks = 0
        vs_files = client.vector_stores.files.list(vector_store_id=vector_store_id)
        for file in vs_files.data:
            total_files += 1
            file_details = client.files.retrieve(file.id)
            chunks = file_details.metadata.get('chunk_count', 1) if hasattr(file_details, 'metadata') else 1
            total_chunks += chunks
        print(f"Sync Summary: {total_files} files embedded, {total_chunks} total chunks")

    # 4. Update Assistant
    my_assistants = client.beta.assistants.list(order="desc", limit=20)
    assistant_id = None
    for ast in my_assistants.data:
        if ast.name == ASSISTANT_NAME:
            assistant_id = ast.id
            break
    
    if assistant_id:
        client.beta.assistants.update(
            assistant_id=assistant_id,
            tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}}
        )
        print(f"Updated Assistant {assistant_id}")
    else:
        ast = client.beta.assistants.create(
            name=ASSISTANT_NAME,
            instructions=SYSTEM_PROMPT,
            model="gpt-4o-mini",
            tools=[{"type": "file_search"}],
            tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}}
        )
        print(f"Created Assistant {ast.id}")