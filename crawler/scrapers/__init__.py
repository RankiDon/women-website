"""Scrapers package."""

from .base_scraper import BaseScraper
from .un_women_scraper import UNWomenScraper
from .who_scraper import WHOScraper
from .undp_scraper import UNDPscraper
from .wikipedia_scraper import WikipediaScraper
from .zh_wikipedia_scraper import ChineseWikipediaScraper

__all__ = [
    'BaseScraper',
    'UNWomenScraper',
    'WHOScraper',
    'UNDPscraper',
    'WikipediaScraper',
    'ChineseWikipediaScraper',
]
