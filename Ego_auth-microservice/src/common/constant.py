from enum import (
    auto,
    Enum
)


class Empty(str, Enum):
    UNSET = auto()
