#!/usr/bin/env python3
"""
Feminist Content Crawler

Crawls feminist content from legitimate sources and stores to database.

Usage:
    python main.py                    # Run all scrapers
    python main.py --source who      # Run WHO scraper
    python main.py --source wikipedia # Run Wikipedia scraper
    python main.py --limit 10       # Limit articles per source
    python main.py --dry-run         # Test without saving
"""

import argparse
import logging
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from crawler.scrapers import (
    UNWomenScraper,
    WHOScraper,
    UNDPscraper,
    WikipediaScraper,
    ChineseWikipediaScraper,
)
from crawler.storage import APIClient, DatabaseStorage
from crawler.config.settings import API_BASE_URL

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


SCRAPERS = {
    'un_women': UNWomenScraper,
    'who': WHOScraper,
    'undp': UNDPscraper,
    'wikipedia': WikipediaScraper,
    'zh_wikipedia': ChineseWikipediaScraper,
}


def run_scraper(scraper_name: str, limit: int, dry_run: bool, api_url: str = None):
    """Run a specific scraper."""
    if scraper_name not in SCRAPERS:
        logger.error(f"Unknown scraper: {scraper_name}")
        return

    scraper_class = SCRAPERS[scraper_name]
    scraper = scraper_class()

    logger.info(f"Starting {scraper.name} scraper...")

    try:
        articles = scraper.scrape(limit=limit)
        logger.info(f"Scraped {len(articles)} articles")

        if not articles:
            logger.warning("No articles scraped")
            return

        if dry_run:
            logger.info("DRY RUN - Articles would be saved:")
            for i, article in enumerate(articles[:5], 1):
                logger.info(f"  {i}. [{article.get('category', 'N/A')}] {article['title'][:60]}...")
                logger.info(f"     Source: {article.get('source_url', 'N/A')[:80]}")
            if len(articles) > 5:
                logger.info(f"  ... and {len(articles) - 5} more")
            return

        # Try API first
        if api_url:
            client = APIClient(api_url)
            saved, skipped = client.save_articles(articles)
        else:
            logger.info("No API available. Set API_BASE_URL or run backend.")
            saved, skipped = 0, len(articles)

        logger.info(f"Results: {saved} saved, {skipped} skipped (duplicates or errors)")

    except Exception as e:
        logger.error(f"Scraper failed: {e}")
        import traceback
        traceback.print_exc()


def main():
    parser = argparse.ArgumentParser(
        description='Crawl feminist content from legitimate sources'
    )
    parser.add_argument(
        '--source', '-s',
        choices=list(SCRAPERS.keys()),
        help='Specific scraper to run'
    )
    parser.add_argument(
        '--limit', '-l',
        type=int, default=None,
        help='Maximum articles per source'
    )
    parser.add_argument(
        '--dry-run', '-d',
        action='store_true',
        help='Test without saving to database'
    )
    parser.add_argument(
        '--api-url',
        default=None,
        help='Backend API URL (overrides config)'
    )
    parser.add_argument(
        '--list',
        action='store_true',
        help='List available scrapers'
    )

    args = parser.parse_args()

    if args.list:
        print("Available scrapers:")
        for name in SCRAPERS.keys():
            print(f"  - {name}")
        return

    api_url = args.api_url or API_BASE_URL

    if args.source:
        run_scraper(args.source, args.limit, args.dry_run, api_url)
    else:
        # Run all scrapers
        for scraper_name in SCRAPERS.keys():
            logger.info(f"\n{'='*50}")
            run_scraper(scraper_name, args.limit, args.dry_run, api_url)


if __name__ == '__main__':
    main()
