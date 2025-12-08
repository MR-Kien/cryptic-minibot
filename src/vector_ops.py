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
    if not client:
        return

    print("Starting Vector Store Sync...")

    # 1. Get/Create Vector Store
    vector_store_id = None
    for vs in client.vector_stores.list().data:
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
    article_to_chunks = {}  # article_id → list of temp paths

    # List và download từ Spaces
    keys = [k for k in list_files(prefix=DATA_PREFIX) if k.endswith('.md')]
    Path("/tmp/data").mkdir(parents=True, exist_ok=True)
    for key in keys:
        filename = os.path.basename(key)
        filepath = os.path.join("/tmp/data", filename)
        download_file(key, filepath)

        # Trích xuất Article ID
        article_id = None
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read(1000)
            match_id = re.search(r'\*\*Article ID:\*\* (\d+)', content)
            if match_id:
                article_id = match_id.group(1)
        except:
            continue
        if not article_id:
            continue

        current_ts = state.get(article_id)
        mapped = openai_map.get(article_id, {})
        old_file_ids = mapped.get("file_ids", [])
        last_synced = mapped.get("synced_at")

        if old_file_ids and last_synced == current_ts:
            continue  # không thay đổi → bỏ qua

        # XÓA chunk cũ
        for old_fid in old_file_ids:
            try:
                client.files.delete(old_fid)
                print(f"Deleted old chunk {old_fid} for art_id {article_id}")
            except Exception as e:
                print(f"Failed to delete {old_fid}: {e}")

        # Preprocess → tạo các chunk
        preprocessed = preprocess_md_with_metadata(filepath, max_subchunk_tokens=600)
        chunk_paths = [p[0] for p in preprocessed]
        article_to_chunks[article_id] = chunk_paths

        for p_path, p_id in preprocessed:
            files_to_upload.append((p_path, p_id, current_ts))

    # 3. UPLOAD + LOG SIÊU CHI TIẾT (đây là phần bạn cần!)
    if files_to_upload:
        print(f"\n{'='*60}")
        print(f"   BẮT ĐẦU UPLOAD {len(files_to_upload)} CHUNK VÀO OPENAI")
        print(f"{'='*60}\n")

        new_map = {}  # article_id → list[file_id]

        for idx, (f_path, art_id, ts) in enumerate(files_to_upload, start=1):
            filename = os.path.basename(f_path)
            print(f"[{idx}/{len(files_to_upload)}] Đang xử lý: {filename} → Article ID: {art_id}")

            try:
                # ───── BƯỚC 1: Upload lên /files (purpose=assistants) ─────
                with open(f_path, "rb") as file_stream:
                    print("   → Bước 1: Đang upload file lên OpenAI /files endpoint...")
                    file_obj = client.files.create(
                        file=file_stream,
                        purpose="assistants"
                    )

                file_id = file_obj.id

                # ───── BƯỚC 2: Attach vào Vector Store ─────
                print(f"   → Bước 2: Attach file_id={file_id} vào Vector Store {vector_store_id}...")
                vs_file_obj = client.vector_stores.files.create(
                    vector_store_id=vector_store_id,
                    file_id=file_id
                )

                print("   ATTACH VÀO VECTOR STORE THÀNH CÔNG!")

                # Lưu file_id (từ /files) để delete sau này
                new_map.setdefault(art_id, []).append(file_id)

            except Exception as e:
                print(f"   FAILED upload/attach {filename}")
                print(f"   Error: {e}")
                import traceback
                traceback.print_exc()
                new_map.setdefault(art_id, []).append("upload_failed")

        # ───── Cập nhật openai_map.json ─────
        print(f"\nCập nhật openai_map.json với {len(new_map)} article(s)...")
        for art_id, file_ids in new_map.items():
            openai_map[art_id] = {
                "file_ids": file_ids,
                "synced_at": state.get(art_id)
            }
            print(f"   → Article {art_id} → file_ids: {file_ids}")

        save_json_to_spaces(openai_map, OPENAI_MAP_KEY)
        print(f"\nOPENAI_MAP.JSON ĐÃ ĐƯỢC CẬP NHẬT THÀNH CÔNG!\n")
        print(f"{'='*60}\n")
       

    # 4. Update Assistant (giữ nguyên)
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
# def sync_vector_store():
#     client = get_client()
#     if not client:
#         return

#     print("Starting Vector Store Sync...")
    
#     # 1. Get/Create Vector Store
#     vector_store_id = None
#     for vs in client.vector_stores.list().data:
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
#     state = load_json_from_spaces(STATE_KEY)
#     openai_map = load_json_from_spaces(OPENAI_MAP_KEY)
    
#     files_to_upload = []
#     article_to_chunks = {}  # article_id → list of temp paths
    
#     # List và download từ Spaces thay vì local dir
#     keys = [k for k in list_files(prefix=DATA_PREFIX) if k.endswith('.md')]
#     Path("/tmp/data").mkdir(parents=True, exist_ok=True)
#     for key in keys:
#         filename = os.path.basename(key)
#         filepath = os.path.join("/tmp/data", filename)
#         download_file(key, filepath)
        
#         # Trích xuất ID từ nội dung file
#         article_id = None
#         try:
#             with open(filepath, 'r', encoding='utf-8') as f:
#                 content = f.read(1000)
#             match_id = re.search(r'\*\*Article ID:\*\* (\d+)', content)
#             if match_id:
#                 article_id = match_id.group(1)
#         except:
#             continue
#         if not article_id:
#             continue
#         current_ts = state.get(article_id)
#         mapped = openai_map.get(article_id, {})
#         old_file_ids = mapped.get("file_ids", [])  # Danh sách nhiều ID
#         last_synced = mapped.get("synced_at")
#         if old_file_ids and last_synced == current_ts:
#             continue
        
#         # XÓA TẤT CẢ chunk cũ
#         for old_fid in old_file_ids:
#             try:
#                 client.files.delete(old_fid)
#                 print(f"Deleted old chunk {old_fid} for art_id {article_id}")
#             except Exception as e:
#                 print(f"Failed to delete {old_fid}: {e}")
        
#         # Preprocess file trước upload
#         preprocessed = preprocess_md_with_metadata(filepath, max_subchunk_tokens=600)
#         chunk_paths = [p[0] for p in preprocessed]
#         article_to_chunks[article_id] = chunk_paths
        
#         for p_path, p_id in preprocessed:
#             files_to_upload.append((p_path, p_id, current_ts))
    
#     # 3. Upload từng file (thay batch để lấy ID trực tiếp - FIX CHÍNH)
#     if files_to_upload:
#         print(f"Uploading {len(files_to_upload)} files individually...")
        
#         # Temp map để cập nhật openai_map sau
#         new_map = {}  # article_id → list of new file_ids
        
#         for idx, (f_path, art_id, ts) in enumerate(files_to_upload):
#             try:
#                 with open(f_path, "rb") as file_stream:
#                     # Upload từng file và lấy ID trực tiếp
#                     response = client.vector_stores.files.create(
#                         vector_store_id=vector_store_id,
#                         file=file_stream
#                     )
#                     file_id = response.id  # ID từ response (VectorStoreFile)
#                     filename = os.path.basename(f_path)
#                     print(f"Uploaded {filename} (chunk {idx+1}) with ID: {file_id}")
                    
#                     # Thêm vào new_map
#                     if art_id not in new_map:
#                         new_map[art_id] = []
#                     new_map[art_id].append(file_id)
                    
#                     # Optional: Sleep ngắn nếu rate limit (thử nếu error)
#                     # import time; time.sleep(0.1)
                    
#             except Exception as e:
#                 print(f"Failed to upload {f_path}: {e}")
#                 # Fallback: Thêm "upload_failed" để debug
#                 if art_id not in new_map:
#                     new_map[art_id] = []
#                 new_map[art_id].append("upload_failed")
        
#         # Cập nhật openai_map với IDs mới
#         for art_id, new_file_ids in new_map.items():
#             openai_map[art_id] = {"file_ids": new_file_ids, "synced_at": state.get(art_id)}
        
#         save_json_to_spaces(openai_map, OPENAI_MAP_KEY)
#         print("Updated openai_map with new file IDs.")
        
#         # Log chunks (giữ nguyên, nhưng giờ total_files chính xác hơn)
#         total_files = 0
#         total_chunks = 0
#         vs_files = client.vector_stores.files.list(vector_store_id=vector_store_id)
#         for file in vs_files.data:
#             total_files += 1
#             file_details = client.files.retrieve(file.id)
#             chunks = file_details.metadata.get('chunk_count', 1) if hasattr(file_details, 'metadata') else 1
#             total_chunks += chunks
#         print(f"Sync Summary: {total_files} files embedded, {total_chunks} total chunks")
    
#     # 4. Update Assistant (giữ nguyên)
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
# def sync_vector_store():
#     client = get_client()
#     if not client:
#         return

#     print("Starting Vector Store Sync...")
    
#     # 1. Get/Create Vector Store
#     vector_store_id = None
#     for vs in client.vector_stores.list().data:
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
#     state = load_json_from_spaces(STATE_KEY)
#     openai_map = load_json_from_spaces(OPENAI_MAP_KEY)
    
#     files_to_upload = []
#     article_to_chunks = {}  # article_id → list of temp paths
    
#     # List và download từ Spaces thay vì local dir
#     keys = [k for k in list_files(prefix=DATA_PREFIX) if k.endswith('.md')]
#     Path("/tmp/data").mkdir(parents=True, exist_ok=True)
#     for key in keys:
#         filename = os.path.basename(key)
#         filepath = os.path.join("/tmp/data", filename)
#         download_file(key, filepath)
        
#         # Trích xuất ID từ nội dung file
#         article_id = None
#         try:
#             with open(filepath, 'r', encoding='utf-8') as f:
#                 content = f.read(1000)
#             match_id = re.search(r'\*\*Article ID:\*\* (\d+)', content)
#             if match_id:
#                 article_id = match_id.group(1)
#         except:
#             continue
#         if not article_id:
#             continue
#         current_ts = state.get(article_id)
#         mapped = openai_map.get(article_id, {})
#         old_file_ids = mapped.get("file_ids", [])  # Danh sách nhiều ID
#         last_synced = mapped.get("synced_at")
#         if old_file_ids and last_synced == current_ts:
#             continue
        
#         # XÓA TẤT CẢ chunk cũ
#         for old_fid in old_file_ids:
#             try:
#                 client.files.delete(old_fid)
#                 print(f"Deleted old chunk {old_fid} for art_id {article_id}")
#             except Exception as e:
#                 print(f"Failed to delete {old_fid}: {e}")
        
#         # Preprocess file trước upload
#         preprocessed = preprocess_md_with_metadata(filepath, max_subchunk_tokens=600)
#         chunk_paths = [p[0] for p in preprocessed]
#         article_to_chunks[article_id] = chunk_paths
        
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
        
#         for f in file_streams:
#             f.close()
        
#         print(f"Batch Status: {file_batch.status}")
        
#         # Lấy list files để map file_id chính xác
#         uploaded_ids = {}  # Map filename -> file_id
#         vs_files = client.vector_stores.files.list(vector_store_id=vector_store_id)
#         for file in vs_files.data:
#             file_details = client.files.retrieve(file.id)
#             if hasattr(file_details, 'filename'):
#                 uploaded_ids[file_details.filename] = file.id
        
#         # Cập nhật map chính xác
#         for article_id, chunk_paths in article_to_chunks.items():
#             new_file_ids = []
#             for path in chunk_paths:
#                 filename = os.path.basename(path)
#                 file_id = uploaded_ids.get(filename, "unknown")
#                 new_file_ids.append(file_id)
#             openai_map[article_id] = {"file_ids": new_file_ids, "synced_at": state.get(article_id)}
        
#         save_json_to_spaces(openai_map, OPENAI_MAP_KEY)
        
#         # Log chunks
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