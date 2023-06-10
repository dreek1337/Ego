import sqlalchemy as sa
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from src.database.models.base import Base


class Users(Base):
    """
    Модель пользователя для бд
    """
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(
        sa.BigInteger,
        primary_key=True
    )
    username: Mapped[str] = mapped_column(sa.String(64))
    password: Mapped[str] = mapped_column(sa.String(55))
    email: Mapped[str] = mapped_column(sa.String())
    deleted: Mapped[bool] = mapped_column(sa.Boolean)
