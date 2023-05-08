from pydantic import BaseModel

from src.domain.models import Post


class Profile(BaseModel):
    """
    Модель профиля
    """
    user: UserProfile
    posts: list[Post]
