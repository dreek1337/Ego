from datetime import datetime
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import (
    Mapped,
    relationship,
    mapped_column
)

from src.infrastructure.database.models.base import Base


class Avatars(Base):
    """
    Таблица для хранения данных аватарки
    """
    __tablename__ = 'avatars'

    avatar_id: Mapped[UUID] = mapped_column(
        sa.Uuid,
        primary_key=True,
        nullable=False,
        autoincrement=False
    )
    avatar_type: Mapped[str] = mapped_column(sa.String(10))
    avatar_content: Mapped[bytes] = mapped_column(sa.LargeBinary, nullable=True)
    avatar_user_id: Mapped[int] = mapped_column(sa.ForeignKey('users.user_id'))

    user = relationship("Users", back_populates="avatar")

    time_updated: Mapped[datetime] = mapped_column(
        sa.DateTime,
        onupdate=sa.func.now(),
        nullable=True
    )
