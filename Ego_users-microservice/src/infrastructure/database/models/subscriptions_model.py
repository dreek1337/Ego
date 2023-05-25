import sqlalchemy as sa
from sqlalchemy.orm import (
    Mapped,
    relationship,
    mapped_column
)

from src.infrastructure.database.models.base import Base
from src.infrastructure.database.models.user_model import Users


class Subscriptions(Base):
    """
    Таблица, которая хранит данные о подписчках пользователей
    """
    __tablename__ = 'subscriptions'
    subscriber_id: Mapped[int] = mapped_column(sa.BigInteger, nullable=False)
    user_id: Mapped[int] = mapped_column(sa.ForeignKey('users.user_id'))

    user: Mapped['Users'] = relationship(back_populates='subscriptions')
