"""Base scraper class for all scrapers."""

from abc import ABC, abstractmethod
from typing import List
import requests
from bs4 import BeautifulSoup
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BaseScraper(ABC):
    """Abstract base class for web scrapers."""

    def __init__(self, name: str, base_url: str):
        self.name = name
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })

    def fetch_page(self, url: str, retries: int = 3) -> BeautifulSoup:
        """Fetch a page and return BeautifulSoup object."""
        for i in range(retries):
            try:
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                return BeautifulSoup(response.content, 'lxml')
            except requests.RequestException as e:
                logger.warning(f"Failed to fetch {url}: {e}")
                if i < retries - 1:
                    time.sleep(2 ** i)
                else:
                    raise

    @abstractmethod
    def get_article_urls(self, page: int = 1) -> List[str]:
        """Get list of article URLs from listing page."""
        pass

    @abstractmethod
    def parse_article(self, url: str) -> dict:
        """Parse a single article and return article data."""
        pass

    def scrape(self, limit: int = None) -> List[dict]:
        """Main scraping method."""
        articles = []
        page = 1

        while True:
            try:
                urls = self.get_article_urls(page)
                if not urls:
                    break

                for url in urls:
                    if limit and len(articles) >= limit:
                        return articles

                    try:
                        article = self.parse_article(url)
                        if article:
                            articles.append(article)
                            logger.info(f"Scraped: {article['title'][:50]}...")
                        time.sleep(1)  # Respectful delay
                    except Exception as e:
                        logger.error(f"Failed to parse {url}: {e}")
                        continue

                page += 1

            except Exception as e:
                logger.error(f"Failed to get article URLs from page {page}: {e}")
                break

        return articles
