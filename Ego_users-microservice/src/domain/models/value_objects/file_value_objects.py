from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class FileUuid:
    value: UUID


@dataclass(frozen=True)
class FileType:
    value: str


@dataclass(frozen=True)
class FileContent:
    value: bytes
