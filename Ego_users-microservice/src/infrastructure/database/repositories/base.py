from sqlalchemy.exc import DBAPIError
from asyncpg import UniqueViolationError  # type: ignore
from sqlalchemy.ext.asyncio import AsyncSession

from src.application import Mapper
from src.application.common import RepoError
from src.domain import (
    AvatarEntity,
    UserAggregate
)
from src.application.user.exceptions import (
    UserIdIsAlreadyExist,
    AvatarIdIsAlreadyExist
)


class SQLAlchemyRepo:
    """
    Базовый класс для репозитория
    """
    def __init__(
            self,
            *,
            session: AsyncSession,
            mapper: Mapper
    ) -> None:
        self._session = session
        self._mapper = mapper

    @staticmethod
    def _parse_error(err: DBAPIError, data: AvatarEntity | UserAggregate) -> None:
        """
        определение ошибки
        """
        error = err.__cause__.__cause__.__class__  # type: ignore

        if error == UniqueViolationError:
            if type(data) == UserAggregate:
                raise UserIdIsAlreadyExist(
                    user_id=data.user_id.to_int
                )
            elif type(data) == AvatarEntity:
                raise AvatarIdIsAlreadyExist(
                    avatar_id=data.avatar_id.to_uuid
                )
        else:
            file_name = __name__
            raise RepoError(file_name=file_name, content=err.args)
