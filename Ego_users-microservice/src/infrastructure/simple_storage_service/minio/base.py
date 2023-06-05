from typing import Any


class MinioBase:
    def __init__(self, session: Any) -> None:
        self._session = session
