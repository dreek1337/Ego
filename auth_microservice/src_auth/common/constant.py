from enum import (
    Enum,
    auto,
)


class Empty(str, Enum):
    UNSET = auto()
