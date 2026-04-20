"""WHO gender health scraper."""

from typing import List
import re
from .base_scraper import BaseScraper


class WHOScraper(BaseScraper):
    """Scraper for WHO gender health articles."""

    CATEGORY_MAP = {
        'health': 'Health',
        'gender': 'Health',
        'women': 'Health',
        'reproductive': 'Health',
        'sexual': 'Health',
        'maternal': 'Health',
        'violence': 'Health',
        'mental': 'Health',
        'hiv': 'Health',
        'cancer': 'Health',
    }

    DEFAULT_CATEGORY = 'Health'

    def __init__(self):
        super().__init__('WHO', 'https://www.who.int')

    def get_article_urls(self, page: int = 1) -> List[str]:
        """Get article URLs from WHO news listing."""
        url = f"{self.base_url}/news/sections"
        soup = self.fetch_page(url)
        if not soup:
            return []

        article_links = []

        # Common link patterns for WHO news
        selectors = [
            'a[href*="/news/"]',
            'a[href*="/mediacentre/"]',
            '.card a[href]',
            '.list-item a[href]',
        ]

        for selector in selectors:
            links = soup.select(selector)
            for link in links:
                href = link.get('href', '')
                if href:
                    # Filter to relevant sections
                    if any(x in href for x in ['/news/', '/mediacentre/']):
                        full_url = href if href.startswith('http') else f"{self.base_url}{href}"
                        if full_url not in article_links:
                            article_links.append(full_url)

        return list(set(article_links))[:15]

    def parse_article(self, url: str) -> dict:
        """Parse a single WHO article."""
        soup = self.fetch_page(url)
        if not soup:
            return None

        title = ''
        content = ''
        category = self.DEFAULT_CATEGORY
        author = 'World Health Organization'
        cover_image = ''

        # Title
        title_elem = soup.select_one('h1') or soup.select_one('meta[property="og:title"]')
        if title_elem:
            title = title_elem.get('content', '') or title_elem.get_text(strip=True)

        if not title:
            return None

        # Cover image
        img_elem = soup.select_one('meta[property="og:image"]') or soup.select_one('article img')
        if img_elem:
            cover_image = img_elem.get('content', '') or img_elem.get('src', '')

        # Content
        content_elem = soup.select_one('article') or soup.select_one('.article-body') or soup.select_one('main')
        if content_elem:
            for tag in content_elem.find_all(['script', 'style', 'nav', 'aside', 'footer', 'header']):
                tag.decompose()
            paragraphs = content_elem.find_all('p')
            content = ' '.join(p.get_text(strip=True) for p in paragraphs)

        content = re.sub(r'\s+', ' ', content).strip()
        content = content[:10000]

        return {
            'title': title,
            'content': content,
            'category': category,
            'author': author,
            'cover_image': cover_image,
            'source_url': url,
            'source_name': self.name,
        }
