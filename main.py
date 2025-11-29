import sys
import os
import logging
import requests  # Cần import thư viện này
import json
from datetime import datetime
from dotenv import load_dotenv # Load biến môi trường
from src.scraper import run_scraper
from src.vector_ops import sync_vector_store

# Load .env
load_dotenv()

# --- LOGGING SETUP ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("job.log", mode='w'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger()

# --- HÀM GỬI DISCORD ---
def send_discord_alert(stats):
    """Gửi báo cáo kết quả về Discord"""
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    
    if not webhook_url:
        logger.warning("No Discord Webhook URL found in .env. Skipping notification.")
        return

    # Tạo màu sắc cho tin nhắn: Xanh lá (thành công) hoặc Vàng (không có gì mới)
    color = 5763719 # Green
    status_text = "Success"
    
    if stats['added'] == 0 and stats['updated'] == 0:
        color = 16776960 # Yellow
        status_text = "No Changes"

    # Cấu trúc tin nhắn (Embed Object)
    payload = {
        "embeds": [{
            "title": f"OptiBot Daily Job Report: {status_text}",
            "description": f"Job finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "color": color,
            "fields": [
                {"name": "Added", "value": str(stats['added']), "inline": True},
                {"name": "Updated", "value": str(stats['updated']), "inline": True},
                {"name": "Skipped", "value": str(stats['skipped']), "inline": True}
            ],
            "footer": {"text": "Running on DigitalOcean • OptiSigns Test"}
        }]
    }

    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            logger.info("Discord notification sent successfully!")
        else:
            logger.error(f"Failed to send Discord. Status: {response.status_code}")
    except Exception as e:
        logger.error(f"Error sending Discord webhook: {e}")

# --- MAIN FUNCTION ---
def main():
    logger.info("========================================")
    logger.info("   OPTIBOT DATA PIPELINE - DAILY JOB    ")
    logger.info("========================================")
    
    try:
        # 1. Scrape
        logger.info("Step 1: Starting Scraper...")
        stats = run_scraper()
        
        logger.info(f"SCRAPER RESULT -> Added: {stats['added']}, Updated: {stats['updated']}, Skipped: {stats['skipped']}")

        # 2. Sync (nếu có thay đổi)
        if stats['added'] > 0 or stats['updated'] > 0:
            logger.info("Change detected. Starting Vector Store Sync...")
            sync_vector_store()
            logger.info("Sync process completed.")
        else:
            logger.info("No content changes detected. Skipping Sync.")

            
        # 3. Gửi thông báo Discord (Bước mới thêm)
        send_discord_alert(stats)

        logger.info("========================================")
        logger.info("JOB FINISHED")

    except Exception as e:
        logger.error(f" FATAL ERROR: {e}", exc_info=True)
        # Gửi cảnh báo lỗi về Discord (Bonus)
        webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
        if webhook_url:
            requests.post(webhook_url, json={"content": f"**JOB FAILED!**\nError: `{str(e)}`"})
        sys.exit(1)

if __name__ == "__main__":
    main()