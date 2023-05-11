from dataclasses import dataclass


@dataclass(frozen=True)
class FileType:
    value: str
