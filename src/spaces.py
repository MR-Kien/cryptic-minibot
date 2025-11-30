# src/spaces.py
import boto3
import os
from botocore.client import Config
from dotenv import load_dotenv
import logging

load_dotenv()

# Cấu hình DigitalOcean Spaces
SPACES_KEY = os.getenv("SPACES_KEY")
SPACES_SECRET = os.getenv("SPACES_SECRET")
SPACES_ENDPOINT = os.getenv("SPACES_ENDPOINT")
SPACES_BUCKET = os.getenv("SPACES_BUCKET")

if not all([SPACES_KEY, SPACES_SECRET, SPACES_BUCKET]):
    raise EnvironmentError("Missing DigitalOcean Spaces credentials in .env")

session = boto3.session.Session()
client = session.client(
    's3',
    config=Config(signature_version='s3v4'),
    endpoint_url=SPACES_ENDPOINT,
    aws_access_key_id=SPACES_KEY,
    aws_secret_access_key=SPACES_SECRET
)

logger = logging.getLogger(__name__)

def upload_file(local_path: str, key: str):
    """Upload file lên Spaces"""
    try:
        client.upload_file(local_path, SPACES_BUCKET, key)
        logger.info(f"Uploaded: {key}")
    except Exception as e:
        logger.error(f"Upload failed {key}: {e}")
        raise

def download_file(key: str, local_path: str):
    """Download file từ Spaces về local"""
    try:
        client.download_file(SPACES_BUCKET, key, local_path)
        logger.info(f"Downloaded: {key}")
    except Exception as e:
        logger.error(f"Download failed {key}: {e}")
        raise

def list_files(prefix: str = ""):
    """Liệt kê file trong bucket"""
    try:
        response = client.list_objects_v2(Bucket=SPACES_BUCKET, Prefix=prefix)
        return [obj['Key'] for obj in response.get('Contents', [])]
    except Exception as e:
        logger.error(f"List files error: {e}")
        return []

def delete_file(key: str):
    """Xóa file trên Spaces"""
    try:
        client.delete_object(Bucket=SPACES_BUCKET, Key=key)
        logger.info(f"Deleted: {key}")
    except Exception as e:
        logger.error(f"Delete failed {key}: {e}")