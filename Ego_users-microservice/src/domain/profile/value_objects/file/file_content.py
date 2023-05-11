from dataclasses import dataclass


@dataclass(frozen=True)
class FileContent:
    value: bytes
