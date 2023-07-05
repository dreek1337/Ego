from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT  # type: ignore
from src.application import AuthService

from ..di.providers import get_auth_jwt_stub, get_service_stub
from .requests.user_requests import UpdateUserRequest
from .responses.user_responses import UpdateUserResponse

user_routers = APIRouter(
    prefix='/auth/user',
    tags=['user']
)


@user_routers.patch(
    path='/update_user',
    responses={
        status.HTTP_200_OK: {'model': UpdateUserResponse}
    },
    response_model=UpdateUserResponse
)
async def update_user_data(
        data: UpdateUserRequest,
        authorize: AuthJWT = Depends(get_auth_jwt_stub),
        service: AuthService = Depends(get_service_stub),

):
    """
    Обнавление данных пользователя
    """
    return await service.update_user_data(data=data, authorize=authorize)
