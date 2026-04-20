"""Configuration settings for the crawler."""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Database settings
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'feminist_women'),
}

# API settings (for backend)
API_BASE_URL = os.getenv('API_BASE_URL', 'http://localhost:8080')

# Scraping settings
REQUEST_DELAY = float(os.getenv('REQUEST_DELAY', 1.0))  # seconds between requests
MAX_RETRIES = int(os.getenv('MAX_RETRIES', 3))
REQUEST_TIMEOUT = 30  # seconds

# Logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
