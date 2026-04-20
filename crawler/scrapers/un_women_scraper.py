"""UN Women news scraper."""

from typing import List
import re
from .base_scraper import BaseScraper


class UNWomenScraper(BaseScraper):
    """Scraper for UN Women news articles."""

    # Category mapping from UN Women topics to our categories
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
    }

    DEFAULT_CATEGORY = 'Politics'

    def __init__(self):
        super().__init__('UN Women', 'https://www.unwomen.org')

    def get_article_urls(self, page: int = 1) -> List[str]:
        """Get article URLs from the news listing page."""
        # UN Women news page - restructured URL format
        if page == 1:
            url = f"{self.base_url}/en/news"
        else:
            url = f"{self.base_url}/en/news?page={page}"

        soup = self.fetch_page(url)
        if not soup:
            return []

        # Try multiple selectors for article links
        article_links = []

        # Newer UN Women structure
        links = soup.select('a[href*="/en/news/"]')
        for link in links:
            href = link.get('href', '')
            # Filter to actual news articles (not category pages)
            if '/news/' in href and not any(x in href for x in ['/en/news/news', '/en/news/all']):
                full_url = href if href.startswith('http') else f"{self.base_url}{href}"
                if full_url not in article_links:
                    article_links.append(full_url)

        return list(set(article_links))[:20]  # Dedupe and limit

    def parse_article(self, url: str) -> dict:
        """Parse a single UN Women article."""
        soup = self.fetch_page(url)
        if not soup:
            return None

        # Try to extract article data
        title = ''
        content = ''
        category = self.DEFAULT_CATEGORY
        author = 'UN Women'
        cover_image = ''

        # Title
        title_elem = soup.select_one('h1') or soup.select_one('h2.article-title') or soup.select_one('[class*="title"]')
        if title_elem:
            title = title_elem.get_text(strip=True)

        # If no title found, skip this article
        if not title:
            return None

        # Cover image
        img_elem = soup.select_one('article img') or soup.select_one('[class*="hero"] img') or soup.select_one('meta[property="og:image"]')
        if img_elem:
            if img_elem.name == 'meta':
                cover_image = img_elem.get('content', '')
            else:
                cover_image = img_elem.get('src', '') or img_elem.get('data-src', '')

        # Content - try multiple selectors
        content_elem = (
            soup.select_one('article [class*="content"]') or
            soup.select_one('article') or
            soup.select_one('[class*="article-body"]') or
            soup.select_one('main')
        )

        if content_elem:
            # Remove unwanted elements
            for tag in content_elem.find_all(['script', 'style', 'nav', 'aside', 'footer', 'header']):
                tag.decompose()

            paragraphs = content_elem.find_all('p')
            content = ' '.join(p.get_text(strip=True) for p in paragraphs)

        # Try to get category from page
        category_elem = soup.select_one('[class*="category"]') or soup.select_one('[class*="topic"]') or soup.select_one('meta[name="category"]')
        if category_elem:
            cat_text = category_elem.get('content', '') or category_elem.get_text(strip=True)
            category = self.map_category(cat_text)

        # Try breadcrumb or tags for category
        breadcrumb = soup.select('a[href*="/en/news/"]')
        for crumb in breadcrumb:
            crumb_text = crumb.get_text(strip=True)
            if crumb_text and crumb_text != 'News':
                mapped = self.map_category(crumb_text)
                if mapped != self.DEFAULT_CATEGORY:
                    category = mapped
                    break

        # Clean content
        content = re.sub(r'\s+', ' ', content).strip()
        content = content[:10000]  # Limit length

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
