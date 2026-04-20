"""API client for storing articles via backend API."""

import requests
import logging
from typing import List, Optional
from ..config.settings import API_BASE_URL

logger = logging.getLogger(__name__)


class APIClient:
    """Client for interacting with the backend API."""

    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        })

    def get_articles(self, page: int = 0, size: int = 100) -> List[dict]:
        """Get existing articles to check for duplicates."""
        try:
            response = self.session.get(
                f"{self.base_url}/api/articles",
                params={'page': page, 'size': size},
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            # Handle both array response and paginated object response
            if isinstance(data, dict):
                return data.get('articles', []) or data.get('content', [])
            return data or []
        except requests.RequestException as e:
            logger.error(f"Failed to fetch articles: {e}")
            return []

    def article_exists(self, source_url: str) -> bool:
        """Check if article with source URL already exists."""
        articles = self.get_articles(size=1000)
        return any(a.get('source_url') == source_url for a in articles)

    def create_article(self, article: dict) -> Optional[int]:
        """Create a new article via API."""
        try:
            response = self.session.post(
                f"{self.base_url}/api/articles",
                json=article,
                timeout=30
            )
            if response.status_code in [200, 201]:
                data = response.json()
                return data.get('id')
            else:
                logger.warning(f"Failed to create article: {response.status_code} - {response.text}")
                return None
        except requests.RequestException as e:
            logger.error(f"Failed to create article: {e}")
            return None

    def save_articles(self, articles: List[dict]) -> tuple:
        """Save multiple articles, skipping duplicates."""
        saved = 0
        skipped = 0

        for article in articles:
            # Check if already exists (skip if duplicate)
            if self.article_exists(article.get('source_url', '')):
                logger.info(f"Skipping duplicate: {article['title'][:50]}...")
                skipped += 1
                continue

            article_id = self.create_article(article)
            if article_id:
                saved += 1
                logger.info(f"Saved: {article['title'][:50]}...")
            else:
                skipped += 1

        return saved, skipped
