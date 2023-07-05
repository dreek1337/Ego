from datetime import date, datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src_users.domain.common import GenderValue
from src_users.infrastructure.database.models.base import Base


class Users(Base):
    """
    Таблица для хранения данные о пользователе
    """

    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(
        sa.BigInteger, primary_key=True, autoincrement=False
    )
    first_name: Mapped[str] = mapped_column(sa.String(length=128), nullable=False)
    last_name: Mapped[str] = mapped_column(sa.String(length=128), nullable=False)
    gender: Mapped[str] = mapped_column(sa.Enum(GenderValue), nullable=False)
    birthday: Mapped[date] = mapped_column(sa.Date, nullable=False)
    deleted: Mapped[bool] = mapped_column(sa.Boolean, default=False)

    avatar = relationship("Avatars", back_populates="user")

    time_updated: Mapped[datetime] = mapped_column(
        sa.DateTime, onupdate=sa.func.now(), nullable=True
    )
