from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class UserBirthday:
    value: datetime
