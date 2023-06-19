import sqlalchemy as sa
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from .base import Base


class Users(Base):
    """
    Модель пользователя для бд
    """
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(
        sa.BigInteger,
        primary_key=True
    )
    username: Mapped[str] = mapped_column(
        sa.String(64),
        unique=True
    )
    salt: Mapped[str] = mapped_column(sa.String())
    password: Mapped[str] = mapped_column(sa.String())
    user_email: Mapped[str] = mapped_column(sa.String())
