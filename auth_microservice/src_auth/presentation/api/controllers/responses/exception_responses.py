from dataclasses import dataclass
from typing import (
    Generic,
    TypeVar,
)

from pydantic.generics import GenericModel

ExcData = TypeVar("ExcData")


@dataclass
class ErrorResult(GenericModel, Generic[ExcData]):
    message: str
    data: ExcData
