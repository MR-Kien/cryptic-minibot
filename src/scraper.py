import os
import json
import requests
import html2text
import re
from pathlib import Path

# --- CONFIG ---
BASE_URL = "https://support.optisigns.com/api/v2/help_center/articles.json"
OUTPUT_DIR = "data"
STATE_FILE = "state.json"

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

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
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    state = load_state()
    converter = init_converter()
    
    url = BASE_URL
    stats = {"added": 0, "updated": 0, "skipped": 0}
    max_pages = 5 
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
                with open(os.path.join(OUTPUT_DIR, filename), 'w', encoding='utf-8') as f:
                    f.write(full_content)
                
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
            
    save_state(state)
    print(f"Scraper Summary: {stats}")
    return stats