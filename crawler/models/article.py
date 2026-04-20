"""Article data model."""

from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class Article:
    """Represents a feminist article."""

    title: str
    content: str
    category: str
    author: str
    cover_image: str = ''
    source_url: str = ''
    source_name: str = ''
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    # Database ID (set after insertion)
    id: Optional[int] = None

    def to_dict(self) -> dict:
        """Convert to dictionary for API/DB."""
        return {
            'title': self.title,
            'content': self.content,
            'category': self.category,
            'author': self.author,
            'cover_image': self.cover_image,
            'source_url': self.source_url,
            'source_name': self.source_name,
        }

    def __str__(self) -> str:
        return f"Article(id={self.id}, title='{self.title[:50]}...')"

    def __repr__(self) -> str:
        return self.__str__()
