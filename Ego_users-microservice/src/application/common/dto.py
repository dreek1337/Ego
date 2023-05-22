from abc import ABC

from pydantic import BaseModel


class DTO(ABC, BaseModel):
    """Базовый класс для DTO"""
    class Config(ABC):
        """Конфигурация модели"""
