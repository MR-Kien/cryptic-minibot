import os
import json
import requests
import html2text
import re
from pathlib import Path
from .spaces import upload_file, download_file  # Chỉ import cần thiết, bỏ client nếu không dùng

# --- CONFIG ---
BASE_URL = "https://support.optisigns.com/api/v2/help_center/articles.json"
STATE_KEY = "state.json"  # Key trên Spaces cho state.json
DATA_PREFIX = "articles/"  # Prefix cho các file .md trên Spaces

def load_json_from_spaces(key):
    temp_path = f"/tmp/{os.path.basename(key)}"
    try:
        download_file(key, temp_path)
        with open(temp_path, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_json_to_spaces(data, key):
    temp_path = f"/tmp/{os.path.basename(key)}"
    with open(temp_path, 'w') as f:
        json.dump(data, f, indent=2)
    upload_file(temp_path, key)

def get_clean_slug(text):
    slug = text.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s-]+', '-', slug).strip('-')
    return slug

def init_converter():
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False 
    h.body_width = 0 
    return h

def run_scraper():
    """Hàm chính để thực hiện việc cào dữ liệu"""
    Path("/tmp/data").mkdir(parents=True, exist_ok=True)  # Sử dụng /tmp cho temp files
    state = load_json_from_spaces(STATE_KEY)
    converter = init_converter()
    
    url = BASE_URL
    stats = {"added": 0, "updated": 0, "skipped": 0}
    max_pages = 5  # Tăng nếu cần nhiều trang hơn
    current_page = 0

    print(f"🕷️  Starting Scraper Job...")

    while url and current_page < max_pages:
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            articles = data.get('articles', [])
            
            for article in articles:
                if article.get('draft', True): continue
                
                art_id = str(article.get('id'))
                remote_updated_at = article.get('updated_at')
                title = article.get('title', 'No Title')
                
                # Logic Delta Check
                last_stored_time = state.get(art_id)
                
                if last_stored_time == remote_updated_at:
                    stats["skipped"] += 1
                    continue
                
                is_update = last_stored_time is not None
                
                body_html = article.get('body', '')
                if not body_html: continue
                
                markdown_content = converter.handle(body_html)
                article_url = article.get('html_url', '')
                
                full_content = (
                    f"# {title}\n"
                    f"**Article URL:** {article_url}\n"
                    f"**Article ID:** {art_id}\n"
                    f"**Updated At:** {remote_updated_at}\n"
                    f"---\n\n"
                    f"{markdown_content}"
                )
                
                slug = get_clean_slug(title)
                filename = f"{slug}.md"
                key = DATA_PREFIX + filename  # Key trên Spaces
                temp_path = f"/tmp/data/{filename}"
                with open(temp_path, 'w', encoding='utf-8') as f:
                    f.write(full_content)
                
                upload_file(temp_path, key)  # Upload lên Spaces
                
                state[art_id] = remote_updated_at
                
                if is_update:
                    print(f"Updated: {title}")
                    stats["updated"] += 1
                else:
                    print(f"Added: {title}")
                    stats["added"] += 1
            
            url = data.get('next_page')
            current_page += 1
            
        except Exception as e:
            print(f"Error scraping: {e}")
            break
            
    save_json_to_spaces(state, STATE_KEY)  # Lưu state lên Spaces
    print(f"Scraper Summary: {stats}")
    return stats