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
    subscription_id: Mapped[sa.BigInteger] = mapped_column(
        sa.ForeignKey('users.user_id')
    )
    subscriber_id: Mapped[sa.BigInteger] = mapped_column(
        sa.ForeignKey('users.user_id')
    )

    user_subscriptions: Mapped['Users'] = relationship(
        back_populates='subscriptions'
    )
    user_subscribers: Mapped['Users'] = relationship(
        back_populates='subscribers'
    )
