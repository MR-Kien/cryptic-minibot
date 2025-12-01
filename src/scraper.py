import os
import json
import requests
import html2text
import re
from pathlib import Path
from .spaces import upload_file, download_file

# --- CONFIG ---
BASE_URL = "https://support.optisigns.com/api/v2/help_center/articles.json"
STATE_KEY = "state.json"
DATA_PREFIX = "articles/"

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
    h.single_line_break = True
    h.inline_links = True
    return h

def fix_code_in_markdown(md: str) -> str:
    """
    Post-process Markdown từ html2text để:
    - Chuyển **sudo raspi-config** → `sudo raspi-config`
    - Chuyển indent 4 spaces → fenced code block ```bash
    - Xử lý các pattern phổ biến của Zendesk
    """
    lines = md.splitlines()
    new_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # 1. Xử lý inline bold dính lệnh: Example: Type**sudo raspi-config** → Type `sudo raspi-config`
        line = re.sub(r'([^\w`])\*\*([^*]+?)\*\*([^\w`]|$)', lambda m: f"{m.group(1)}`{m.group(2)}`{m.group(3)}", line)

        # 2. Nếu dòng bắt đầu bằng 4+ khoảng trắng → chuyển thành fenced block
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        if indent >= 4 and stripped.strip():
            # Gom tất cả các dòng indent liên tiếp thành 1 code block
            code_lines = [stripped]
            i += 1
            while i < len(lines):
                next_line = lines[i]
                next_stripped = next_line.lstrip()
                next_indent = len(next_line) - len(next_stripped)
                if next_indent >= 4 and next_stripped.strip():
                    code_lines.append(next_stripped)
                    i += 1
                else:
                    break
            # Thêm fenced block
            new_lines.append("")  # dòng trống trước block
            new_lines.append("```bash")
            new_lines.extend(code_lines)
            new_lines.append("```")
            new_lines.append("")  # dòng trống sau block
            continue  # đã xử lý xong block này

        # 3. Các pattern đặc biệt của Zendesk (Type/Run/Enter + lệnh bold)
        line = re.sub(
            r'(?i)(type|run|enter|execute) ?\*\*(.+?)\*\* ?(.*terminal.*)?',
            r'\1:\n\n```\2\n```\n\3'.strip(),
            line,
            flags=re.IGNORECASE
        )

        new_lines.append(line)
        i += 1

    return "\n".join(new_lines).strip() + "\n"

def run_scraper():
    """Hàm chính để thực hiện việc cào dữ liệu"""
    Path("/tmp/data").mkdir(parents=True, exist_ok=True)
    state = load_json_from_spaces(STATE_KEY)
    converter = init_converter()
    
    url = BASE_URL
    stats = {"added": 0, "updated": 0, "skipped": 0}
    max_pages = 15  # Đề xuất tăng lên để lấy hết ~398 bài
    current_page = 0

    print("Starting Scraper Job...")

    while url and current_page < max_pages:
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            articles = data.get('articles', [])
            
            for article in articles:
                if article.get('draft', True):
                    continue
                
                art_id = str(article.get('id'))
                remote_updated_at = article.get('updated_at')
                title = article.get('title', 'No Title')
                
                # Delta check
                if state.get(art_id) == remote_updated_at:
                    stats["skipped"] += 1
                    continue
                
                is_update = art_id in state
                
                body_html = article.get('body') or ''
                if not body_html:
                    continue
                
                # Convert HTML → Markdown thô
                markdown_content = converter.handle(body_html)
                
                # QUAN TRỌNG: Fix code ở đây
                markdown_content = fix_code_in_markdown(markdown_content)
                
                article_url = article.get('html_url', '')
                
                full_content = (
                    f"# {title}\n"
                    f"**Article URL:** {article_url}\n"
                    f"**Article ID:** {art_id}\n"
                    f"**Updated At:** {remote_updated_at}\n"
                    f"---\n\n"
                    f"{markdown_content.strip()}\n"
                )
                
                slug = get_clean_slug(title)
                filename = f"{slug}.md"
                key = DATA_PREFIX + filename
                temp_path = f"/tmp/data/{filename}"
                
                with open(temp_path, 'w', encoding='utf-8') as f:
                    f.write(full_content)
                
                upload_file(temp_path, key)
                
                state[art_id] = remote_updated_at
                
                action = "Updated" if is_update else "Added"
                print(f"{action}: {title}")
                stats["updated" if is_update else "added"] += 1
            
            url = data.get('next_page')
            current_page += 1
            
        except Exception as e:
            print(f"Error scraping: {e}")
            break
            
    save_json_to_spaces(state, STATE_KEY)
    print(f"Scraper Summary: {stats}")
    return stats