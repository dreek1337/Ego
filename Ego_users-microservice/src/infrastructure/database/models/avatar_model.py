from datetime import datetime
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import (
    Mapped,
    relationship,
    mapped_column
)

from src.domain.user.value_objects import AvatarType
from src.infrastructure.database.models.base import Base
from src.infrastructure.database.models.user_model import Users


class Avatars(Base):
    """
    Таблица для хранения данных аватарки
    """
    __tablename__ = 'avatars'

    avatar_id: Mapped[UUID] = mapped_column(sa.Uuid, nullable=False)
    avatar_type: Mapped[str] = mapped_column(sa.Enum(AvatarType))
    avatar_content: Mapped[bytes] = mapped_column(sa.LargeBinary, nullable=True)
    user_id: Mapped[int] = mapped_column(sa.ForeignKey('users.user_id'))

    user: Mapped['Users'] = relationship(back_populates='avatar')

    time_updated: Mapped[datetime] = mapped_column(sa.DateTime, onupdate=sa.func.now())
