from pydantic import (
    BaseModel,
    Field
)


class Subscription(BaseModel):
    """
    Модель подписок
    """
    user_id: int = Field(..., 'Айди на кого подписаны')
    subscriber_id: int = Field(..., 'Айди подписчика')
