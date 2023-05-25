from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    """Базовый класс моделей орм"""
    time_created: Mapped[datetime] = mapped_column(
        sa.DateTime,
        server_default=sa.func.now()
    )
