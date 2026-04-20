"""UN Women news scraper - alternative approach using RSS/JSON."""

from typing import List
import re
import json
from .base_scraper import BaseScraper


class UNWomenScraper(BaseScraper):
    """Scraper for UN Women news articles."""

    CATEGORY_MAP = {
        'Women and the Economy': 'Workplace',
        'Violence against Women': 'Health',
        'Women in Politics': 'Politics',
        'Education': 'Education',
        'Climate': 'Activism',
        'Culture': 'Culture',
        'Health': 'Health',
        'Peace': 'Activism',
        'Migration': 'Politics',
        'Armed Conflict': 'Activism',
        'Human Rights': 'Activism',
        'Women Leaders': 'Workplace',
        'COVID-19': 'Health',
        'Financing': 'Politics',
        'Gender Equality': 'Politics',
        'stories': 'Culture',
        'press-release': 'Politics',
        'statement': 'Politics',
        'speech': 'Politics',
        'campaign': 'Activism',
    }

    DEFAULT_CATEGORY = 'Politics'

    def __init__(self):
        super().__init__('UN Women', 'https://www.unwomen.org')
        # Try to use API endpoint instead of web scraping
        self.api_url = 'https://api.helloio.app/v1/news/list'

    def get_article_urls(self, page: int = 1) -> List[str]:
        """Get article URLs from listing page."""
        # Try the news API endpoint
        try:
            # UN Women often has a JSON-based news listing
            url = f"{self.base_url}/api/news/newsListing?page={page}&size=20&lang=en"
            soup = self.fetch_page(url)
            if soup:
                # Try to find JSON data in page
                scripts = soup.find_all('script', type='application/ld+json')
                for script in scripts:
                    try:
                        data = json.loads(script.string)
                        if '@type' in data and data['@type'] == 'NewsArticle':
                            return [data.get('url', '')]
                    except:
                        pass
        except Exception:
            pass

        # Fallback: try direct page with different approach
        url = f"{self.base_url}/en/news"
        soup = self.fetch_page(url)
        if not soup:
            return []

        article_links = []

        # Look for article links in common patterns
        selectors = [
            'article a[href*="/news/"]',
            'a[href*="/en/news/"]',
            '.card a[href]',
            '.article-card a[href]',
            '.news-item a[href]',
        ]

        for selector in selectors:
            links = soup.select(selector)
            for link in links:
                href = link.get('href', '')
                if href and '/news/' in href and 'unwomen.org' in href or href.startswith('/en/news/'):
                    full_url = href if href.startswith('http') else f"{self.base_url}{href}"
                    if full_url not in article_links:
                        article_links.append(full_url)

        return list(set(article_links))[:20]

    def parse_article(self, url: str) -> dict:
        """Parse a single UN Women article."""
        soup = self.fetch_page(url)
        if not soup:
            return None

        title = ''
        content = ''
        category = self.DEFAULT_CATEGORY
        author = 'UN Women'
        cover_image = ''

        # Title
        title_elem = (
            soup.select_one('h1') or
            soup.select_one('h1.article-title') or
            soup.select_one('[class*="title"]') or
            soup.select_one('meta[property="og:title"]')
        )
        if title_elem:
            title = title_elem.get('content', '') or title_elem.get_text(strip=True)

        if not title:
            return None

        # Cover image
        img_elem = (
            soup.select_one('article img') or
            soup.select_one('meta[property="og:image"]') or
            soup.select_one('meta[name="twitter:image"]')
        )
        if img_elem:
            cover_image = img_elem.get('content', '') or img_elem.get('src', '')

        # Content
        content_elem = (
            soup.select_one('article [class*="content"]') or
            soup.select_one('article') or
            soup.select_one('[class*="article-body"]') or
            soup.select_one('main')
        )

        if content_elem:
            for tag in content_elem.find_all(['script', 'style', 'nav', 'aside', 'footer', 'header']):
                tag.decompose()

            paragraphs = content_elem.find_all('p')
            content = ' '.join(p.get_text(strip=True) for p in paragraphs)

        # Category from page
        category_elem = soup.select_one('[class*="category"]')
        if category_elem:
            category = self.map_category(category_elem.get_text(strip=True))

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

    def map_category(self, text: str) -> str:
        """Map UN Women category to our category."""
        text = text.strip()
        for key, value in self.CATEGORY_MAP.items():
            if key.lower() in text.lower():
                return value
        return self.DEFAULT_CATEGORY
