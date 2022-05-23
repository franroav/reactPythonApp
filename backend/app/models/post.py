from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime


class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: Optional[bool] = False


# post = relationship("Post", back_populates="owner")
