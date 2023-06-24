from dataclasses import dataclass

from src.application import AppException


@dataclass
class UnsupportedConvertor(AppException):
    """
    Нет подходящего Convertor
    """
    @property
    def message(self) -> str:
        """
        Сообщение об ошибке
        """
        return 'ToModel or FromModel is unsupported!'
