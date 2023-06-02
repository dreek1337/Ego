from typing import Generic, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

TData = TypeVar("TData")


class ErrorResult(GenericModel, Generic[TData], BaseModel):
    message: str
    data: TData

    class Config:
        frozen = True
