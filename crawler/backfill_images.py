#!/usr/bin/env python3
"""Backfill cover images for articles using Wikipedia API."""

import requests
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from crawler.storage import APIClient

API_BASE = "http://123.57.174.238"

UNSPLASH_MAP = {
    '政治': 'https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?w=800',
    'Politics': 'https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?w=800',
    '健康': 'https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=800',
    'Health': 'https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=800',
    '教育': 'https://images.unsplash.com/photo-1523580494863-6f3031224c94?w=800',
    'Education': 'https://images.unsplash.com/photo-1523580494863-6f3031224c94?w=800',
    '职场': 'https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=800',
    'Workplace': 'https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=800',
    '文化': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800',
    'Culture': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800',
    '行动主义': 'https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=800',
    'Activism': 'https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=800',
}


def get_wikipedia_thumbnail(title, lang='zh'):
    """Get thumbnail from Wikipedia REST API."""
    base = f'https://{lang}.wikipedia.org/api/rest_v1/page/summary/'
    try:
        resp = requests.get(base + title, headers={
            'User-Agent': 'WomenWebsite/1.0 (feminist content curation)'
        }, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            thumb = data.get('thumbnail', {}).get('source', '')
            if thumb:
                return thumb
            orig = data.get('originalimage', {}).get('source', '')
            if orig:
                return orig
    except Exception:
        pass
    return None


def main():
    client = APIClient(API_BASE)
    articles = client.get_articles(page=0, size=200)

    updated = 0
    for article in articles:
        if article.get('coverImage') and article['coverImage'] != '':
            continue

        article_id = article['id']
        title = article['title']
        category = article.get('category', '')

        # Try Wikipedia API for thumbnail
        image_url = None
        # Try Chinese Wikipedia first
        image_url = get_wikipedia_thumbnail(title, 'zh')
        if not image_url:
            # Try English Wikipedia
            image_url = get_wikipedia_thumbnail(title, 'en')

        # Fallback to Unsplash by category
        if not image_url:
            image_url = UNSPLASH_MAP.get(category)

        if image_url:
            try:
                resp = requests.put(
                    f'{API_BASE}/api/articles/{article_id}',
                    json={'title': title, 'content': article['content'],
                          'category': category, 'author': article.get('author', ''),
                          'coverImage': image_url},
                    timeout=10
                )
                if resp.ok:
                    updated += 1
                    print(f'  ✓ {title[:50]} -> {image_url[:60]}')
                else:
                    print(f'  ✗ {title[:50]} HTTP {resp.status_code}')
            except Exception as e:
                print(f'  ✗ {title[:50]} {e}')

    print(f'\nUpdated {updated} articles')


if __name__ == '__main__':
    main()
