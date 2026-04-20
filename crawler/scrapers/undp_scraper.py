"""UNDP gender scraper."""

from typing import List
import re
from .base_scraper import BaseScraper


class UNDPscraper(BaseScraper):
    """Scraper for UNDP gender equality articles."""

    CATEGORY_MAP = {
        'gender': 'Politics',
        'women': 'Politics',
        'equality': 'Politics',
        'empowerment': 'Workplace',
        'economy': 'Workplace',
        'health': 'Health',
        'education': 'Education',
        'leadership': 'Workplace',
        'climate': 'Activism',
        'poverty': 'Politics',
    }

    DEFAULT_CATEGORY = 'Politics'

    def __init__(self):
        super().__init__('UNDP', 'https://www.undp.org')

    def get_article_urls(self, page: int = 1) -> List[str]:
        """Get article URLs from UNDP news."""
        url = f"{self.base_url}/news"
        soup = self.fetch_page(url)
        if not soup:
            return []

        article_links = []
        selectors = [
            'a[href*="/news/"]',
            'a[href*="/development-posts/"]',
            '.card a[href]',
        ]

        for selector in selectors:
            links = soup.select(selector)
            for link in links:
                href = link.get('href', '')
                if href and '/news/' in href:
                    full_url = href if href.startswith('http') else f"{self.base_url}{href}"
                    if full_url not in article_links:
                        article_links.append(full_url)

        return list(set(article_links))[:15]

    def parse_article(self, url: str) -> dict:
        """Parse a single UNDP article."""
        soup = self.fetch_page(url)
        if not soup:
            return None

        title = ''
        content = ''
        category = self.DEFAULT_CATEGORY
        author = 'UNDP'
        cover_image = ''

        title_elem = soup.select_one('h1') or soup.select_one('meta[property="og:title"]')
        if title_elem:
            title = title_elem.get('content', '') or title_elem.get_text(strip=True)

        if not title:
            return None

        img_elem = soup.select_one('meta[property="og:image"]')
        if img_elem:
            cover_image = img_elem.get('content', '')

        content_elem = soup.select_one('article') or soup.select_one('.field-name-body') or soup.select_one('main')
        if content_elem:
            for tag in content_elem.find_all(['script', 'style', 'nav', 'aside', 'footer']):
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
