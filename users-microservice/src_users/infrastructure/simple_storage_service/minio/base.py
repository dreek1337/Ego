from typing import AsyncContextManager, Callable


class MinioCloudStorageImpl:
    """
    Реализация работы с с3
    """

    def __init__(self, connection: Callable[..., AsyncContextManager]) -> None:
        self._connection = connection
