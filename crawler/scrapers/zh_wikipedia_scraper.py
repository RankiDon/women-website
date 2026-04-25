"""Chinese Wikipedia scraper for feminist content."""

from typing import List
import re
from .base_scraper import BaseScraper


class ChineseWikipediaScraper(BaseScraper):
    """Scraper for Chinese Wikipedia feminist content (CC BY-SA license)."""

    CATEGORY_MAP = {
        '女权': '政治',
        '女性': '政治',
        '性别': '政治',
        '平等': '政治',
        '生育': '健康',
        '生殖': '健康',
        '暴力': '健康',
        '教育': '教育',
        '职场': '职场',
        '工作': '职场',
        '文化': '文化',
        '运动': '行动主义',
        '理论': '教育',
        '母亲': '健康',
        '歧视': '政治',
        '堕胎': '健康',
        '避孕': '健康',
        '父权': '政治',
        '选举': '政治',
        '骚扰': '职场',
        '薪资': '职场',
        '领导': '职场',
        '发展': '教育',
        '健康': '健康',
        '家暴': '健康',
        '主义': '行动主义',
        '美': '文化',
        '艺术': '文化',
        '权益': '政治',
        '参政': '政治',
    }

    DEFAULT_CATEGORY = '政治'

    def __init__(self):
        super().__init__('中文维基百科', 'https://zh.wikipedia.org')

    def get_article_urls(self, page: int = 1) -> List[str]:
        """Get Chinese Wikipedia article URLs related to feminism."""
        urls = [
            # Core feminism
            f"{self.base_url}/wiki/女权主义",
            f"{self.base_url}/wiki/女性主义",
            f"{self.base_url}/wiki/女权主义历史",
            f"{self.base_url}/wiki/妇女权利",
            f"{self.base_url}/wiki/性别平等",
            f"{self.base_url}/wiki/交叉性",
            f"{self.base_url}/wiki/女性参政",
            f"{self.base_url}/wiki/性骚扰",
            f"{self.base_url}/wiki/家庭暴力",
            f"{self.base_url}/wiki/生育权",
            f"{self.base_url}/wiki/同工同酬",
            f"{self.base_url}/wiki/妇女参政论",
            f"{self.base_url}/wiki/女权主义运动",
            f"{self.base_url}/wiki/女性主义理论",
            f"{self.base_url}/wiki/性别研究",
            f"{self.base_url}/wiki/性别薪酬差距",
            f"{self.base_url}/wiki/性别歧视",
            f"{self.base_url}/wiki/父权制",
            f"{self.base_url}/wiki/厌女症",
            f"{self.base_url}/wiki/职场女性",
            f"{self.base_url}/wiki/孕产妇健康",
            f"{self.base_url}/wiki/堕胎",
            f"{self.base_url}/wiki/避孕",
            f"{self.base_url}/wiki/生殖健康",
            f"{self.base_url}/wiki/女性发展",
            f"{self.base_url}/wiki/妇女赋权",
            f"{self.base_url}/wiki/性别暴力",
            f"{self.base_url}/wiki/自由主义女权主义",
            f"{self.base_url}/wiki/激进女权主义",
            f"{self.base_url}/wiki/社会主义女权主义",
            f"{self.base_url}/wiki/反女权主义",
            f"{self.base_url}/wiki/中华全国妇女联合会",
            f"{self.base_url}/wiki/妇女劳动权",
            f"{self.base_url}/wiki/妇女教育",
            f"{self.base_url}/wiki/女性生殖器切割",
            f"{self.base_url}/wiki/重男轻女",
            f"{self.base_url}/wiki/女性主义电影",
            f"{self.base_url}/wiki/性別角色",
            f"{self.base_url}/wiki/亲密伴侣暴力",
            f"{self.base_url}/wiki/女权主义经济学",
            # More topics
            f"{self.base_url}/wiki/婦女研究",
            f"{self.base_url}/wiki/身体自主权",
            f"{self.base_url}/wiki/婚姻法",
            f"{self.base_url}/wiki/月经羞耻",
            f"{self.base_url}/wiki/性別主流化",
            f"{self.base_url}/wiki/女性主義文學",
            f"{self.base_url}/wiki/女書",
            f"{self.base_url}/wiki/三八婦女節",
            f"{self.base_url}/wiki/反性骚扰运动",
            f"{self.base_url}/wiki/MeToo运动",
        ]
        return urls

    def parse_article(self, url: str) -> dict:
        """Parse a single Chinese Wikipedia article."""
        soup = self.fetch_page(url)
        if not soup:
            return None

        title_elem = soup.select_one('#firstHeading') or soup.select_one('h1')
        title = title_elem.get_text(strip=True) if title_elem else ''

        if not title:
            return None

        author = '维基百科 (CC BY-SA 3.0)'

        cover_image = ''
        img_elem = soup.select_one('.infobox img') or soup.select_one('#content img')
        if img_elem:
            cover_image = img_elem.get('src', '')
            if cover_image and not cover_image.startswith('http'):
                cover_image = 'https:' + cover_image

        content_elem = soup.select_one('#mw-content-text') or soup.select_one('#content')
        content = ''
        if content_elem:
            for tag in content_elem.find_all(['script', 'style', 'table']):
                tag.decompose()

            paragraphs = content_elem.find_all('p')[:50]
            content = ' '.join(p.get_text(strip=True) for p in paragraphs)

        # Determine category
        url_lower = url.lower()
        category = self.DEFAULT_CATEGORY
        for key, value in self.CATEGORY_MAP.items():
            if key in url_lower:
                category = value
                break

        content = re.sub(r'\s+', ' ', content).strip()
        content = content[:8000]

        return {
            'title': title,
            'content': content,
            'category': category,
            'author': author,
            'cover_image': cover_image,
            'source_url': url,
            'source_name': self.name,
        }
