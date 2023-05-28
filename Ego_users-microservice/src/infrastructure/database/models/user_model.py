from datetime import (
    date,
    datetime
)

import sqlalchemy as sa
from sqlalchemy.orm import (
    Mapped,
    relationship,
    mapped_column
)

from src.domain.common import GenderValue
from src.infrastructure.database.models.base import Base
from src.infrastructure.database.models.avatar_model import Avatars
from src.infrastructure.database.models.subscriptions_model import Subscriptions


class Users(Base):
    """
    Таблица для хранения данные о пользователе
    """
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(
        sa.BigInteger,
        primary_key=True,
        autoincrement=False
    )
    first_name: Mapped[str] = mapped_column(sa.String(length=128), nullable=False)
    last_name: Mapped[str] = mapped_column(sa.String(length=128), nullable=False)
    gender: Mapped[str] = mapped_column(sa.Enum(GenderValue), nullable=False)
    birthday: Mapped[date] = mapped_column(sa.Date, nullable=False)
    deleted: Mapped[bool] = mapped_column(sa.Boolean, default=False)

    avatar: Mapped['Avatars'] = relationship(
        back_populates='user'
    )
    subscriptions: Mapped['Subscriptions'] = relationship(
        back_populates='user_subscriptions'
    )
    subscribers: Mapped['Subscriptions'] = relationship(
        back_populates='user_subscribers'
    )

    time_updated: Mapped[datetime] = mapped_column(sa.DateTime, onupdate=sa.func.now())
