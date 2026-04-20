"""Direct database storage for articles."""

try:
    import mysql.connector
    from mysql.connector import Error
    MYSQL_AVAILABLE = True
except ImportError:
    MYSQL_AVAILABLE = False
    Error = Exception

import logging
from typing import List, Optional
from ..config.settings import DB_CONFIG
from ..models.article import Article

logger = logging.getLogger(__name__)


class DatabaseStorage:
    """Direct MySQL database storage."""

    def __init__(self, config: dict = None):
        self.config = config or DB_CONFIG
        self.connection = None

    def connect(self):
        """Establish database connection."""
        try:
            self.connection = mysql.connector.connect(**self.config)
            logger.info("Database connected successfully")
        except Error as e:
            logger.error(f"Failed to connect to database: {e}")
            raise

    def close(self):
        """Close database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            logger.info("Database connection closed")

    def _ensure_connection(self):
        """Ensure connection is active."""
        if not self.connection or not self.connection.is_connected():
            self.connect()

    def article_exists(self, source_url: str) -> bool:
        """Check if article with source URL exists."""
        self._ensure_connection()
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT COUNT(*) FROM articles WHERE source_url = %s",
                (source_url,)
            )
            count = cursor.fetchone()[0]
            return count > 0
        finally:
            cursor.close()

    def save_article(self, article: Article) -> Optional[int]:
        """Save article to database."""
        self._ensure_connection()
        cursor = self.connection.cursor()

        try:
            # Check for duplicate
            if self.article_exists(article.source_url):
                logger.info(f"Skipping duplicate: {article.title[:50]}...")
                return None

            query = """
                INSERT INTO articles (title, content, category, author, cover_image, source_url, created_at, updated_at)
                VALUES (%s, %s, %s, %s, %s, %s, NOW(), NOW())
            """
            values = (
                article.title,
                article.content,
                article.category,
                article.author,
                article.cover_image,
                article.source_url,
            )

            cursor.execute(query, values)
            self.connection.commit()
            article_id = cursor.lastrowid
            logger.info(f"Saved: {article.title[:50]}...")
            return article_id

        except Error as e:
            logger.error(f"Failed to save article: {e}")
            self.connection.rollback()
            return None
        finally:
            cursor.close()

    def save_articles(self, articles: List[Article]) -> tuple:
        """Save multiple articles."""
        saved = 0
        skipped = 0

        for article in articles:
            if isinstance(article, dict):
                article = Article(**article)

            result = self.save_article(article)
            if result:
                saved += 1
            else:
                skipped += 1

        return saved, skipped

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
