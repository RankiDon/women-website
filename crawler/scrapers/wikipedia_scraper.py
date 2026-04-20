"""Wikipedia CC-licensed content scraper."""

from typing import List
import re
from .base_scraper import BaseScraper


class WikipediaScraper(BaseScraper):
    """Scraper for Wikipedia feminist content (CC BY-SA license)."""

    CATEGORY_MAP = {
        'feminism': 'Politics',
        'gender': 'Politics',
        'women': 'Politics',
        'equality': 'Politics',
        'reproductive': 'Health',
        'violence': 'Health',
        'workplace': 'Workplace',
        'education': 'Education',
        'history': 'Culture',
        'movement': 'Activism',
        'theory': 'Education',
        'mother': 'Health',
        'beauty': 'Culture',
        'objectification': 'Culture',
        'discrimination': 'Politics',
        'abortion': 'Health',
        'contraception': 'Health',
        'maternal': 'Health',
        'patriarchy': 'Politics',
        'sexism': 'Politics',
        'harassment': 'Workplace',
        'pay': 'Workplace',
        'leadership': 'Workplace',
        'suffrage': 'Politics',
        'waves': 'Culture',
        'feminist': 'Politics',
    }

    DEFAULT_CATEGORY = 'Politics'

    def __init__(self):
        super().__init__('Wikipedia', 'https://en.wikipedia.org')

    def get_article_urls(self, page: int = 1) -> List[str]:
        """Get Wikipedia article URLs related to feminism."""
        urls = [
            # Core feminism topics
            f"{self.base_url}/wiki/Feminism",
            f"{self.base_url}/wiki/History_of_feminism",
            f"{self.base_url}/wiki/Women%27s_rights",
            f"{self.base_url}/wiki/Gender_equality",
            f"{self.base_url}/wiki/Intersectionality",
            f"{self.base_url}/wiki/Women_in_politics",
            f"{self.base_url}/wiki/Sexual_harassment",
            f"{self.base_url}/wiki/Domestic_violence",
            f"{self.base_url}/wiki/Reproductive_rights",
            f"{self.base_url}/wiki/Equal_pay",
            # Additional topics
            f"{self.base_url}/wiki/Women%27s_suffrage",
            f"{self.base_url}/wiki/Feminist_movement",
            f"{self.base_url}/wiki/Feminist_theory",
            f"{self.base_url}/wiki/Feminist_economics",
            f"{self.base_url}/wiki/Gender_studies",
            f"{self.base_url}/wiki/Gender_pay_gap",
            f"{self.base_url}/wiki/Sexism",
            f"{self.base_url}/wiki/Patriarchy",
            f"{self.base_url}/wiki/Gender_discrimination",
            f"{self.base_url}/wiki/Misogyny",
            f"{self.base_url}/wiki/Women_in_the_workplace",
            f"{self.base_url}/wiki/Maternal_health",
            f"{self.base_url}/wiki/Abortion",
            f"{self.base_url}/wiki/Contraception",
            f"{self.base_url}/wiki/Sexual_and_reproductive_health",
            f"{self.base_url}/wiki/Women_in_development",
            f"{self.base_url}/wiki/Women%27s_empowerment",
            f"{self.base_url}/wiki/Gender-based_violence",
            f"{self.base_url}/wiki/Cultural_feminism",
            f"{self.base_url}/wiki/Radical_feminism",
            f"{self.base_url}/wiki/Liberal_feminism",
            f"{self.base_url}/wiki/Marxist_feminism",
            f"{self.base_url}/wiki/Postmodern_feminism",
            f"{self.base_url}/wiki/Third-wave_feminism",
            f"{self.base_url}/wiki/Fourth-wave_feminism",
            f"{self.base_url}/wiki/Feminism_in_the_United_States",
            f"{self.base_url}/wiki/Feminism_in_Europe",
            f"{self.base_url}/wiki/Feminism_in_Asia",
            f"{self.base_url}/wiki/Islamic_feminism",
            f"{self.base_url}/wiki/Chinawomen%27s_movement",
            f"{self.base_url}/wiki/Anti-feminism",
        ]
        return urls

    def parse_article(self, url: str) -> dict:
        """Parse a single Wikipedia article."""
        soup = self.fetch_page(url)
        if not soup:
            return None

        # Extract title
        title_elem = soup.select_one('#firstHeading') or soup.select_one('h1')
        title = title_elem.get_text(strip=True) if title_elem else ''

        if not title:
            return None

        # Wikipedia is CC BY-SA, attribute in author
        author = 'Wikipedia (CC BY-SA 3.0)'

        # Cover image
        cover_image = ''
        img_elem = soup.select_one('.mw.wiki-logo') or soup.select_one('.infobox img') or soup.select_one('#content img')
        if img_elem:
            cover_image = img_elem.get('src', '')
            if cover_image and not cover_image.startswith('http'):
                cover_image = 'https:' + cover_image

        # Content from paragraphs
        content_elem = soup.select_one('#mw-content-text') or soup.select_one('#content')
        if content_elem:
            for tag in content_elem.find_all(['script', 'style', '.navbox', '. infobox', '.metadata', '.printfooter']):
                tag.decompose()

            paragraphs = content_elem.find_all('p')[:50]  # First 50 paragraphs
            content = ' '.join(p.get_text(strip=True) for p in paragraphs)

        # Determine category from URL/title
        url_lower = url.lower()
        category = self.DEFAULT_CATEGORY
        for key, value in self.CATEGORY_MAP.items():
            if key in url_lower:
                category = value
                break

        content = re.sub(r'\s+', ' ', content).strip()
        content = content[:8000]  # Limit length

        return {
            'title': title,
            'content': content,
            'category': category,
            'author': author,
            'cover_image': cover_image,
            'source_url': url,
            'source_name': self.name,
        }
