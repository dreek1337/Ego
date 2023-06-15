from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    DeclarativeBase
)


class Base(DeclarativeBase):
    """Базовый класс моделей орм"""
    time_created: Mapped[datetime] = mapped_column(
        sa.DateTime,
        server_default=sa.func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        sa.DateTime,
        nullable=True,
        onupdate=sa.func.now()
    )
