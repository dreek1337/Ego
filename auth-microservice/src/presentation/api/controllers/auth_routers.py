from fastapi import (
    status,
    Depends,
    Response,
    APIRouter
)
from fastapi_jwt_auth import AuthJWT  # type: ignore


from src.application import AuthService
from .responses.exception_responses import ErrorResult
from ..di.providers import (
    get_service_stub,
    get_auth_jwt_stub
)
from .requests.auth_requests import (
    LoginRequest,
    RegistrationRequest
)
from .responses.auth_response import (
    TokensResponse,
    RefreshTokenResponse
)
from src.application.exceptions import (
    UserIdIsNotExists,
    UserDataIsNotCorrect,
    UsernameIsAlreadyExist
)

auth_routers = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@auth_routers.post(
    path='/registration',
    responses={
        status.HTTP_200_OK: {'model': TokensResponse},
        status.HTTP_409_CONFLICT: {
            'model': ErrorResult[UsernameIsAlreadyExist]
        }
    },
    response_model=TokensResponse
)
async def user_registration(
        data: RegistrationRequest,
        authorize: AuthJWT = Depends(get_auth_jwt_stub),
        service: AuthService = Depends(get_service_stub)
):
    """
    Регистрация пользователя
    """
    return await service.registration_user(data=data, authorize=authorize)


@auth_routers.post(
    path='/login',
    responses={
        status.HTTP_200_OK: {'model': TokensResponse},
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorResult[UserDataIsNotCorrect]
        }
    },
    response_model=TokensResponse
)
async def user_login(
        data: LoginRequest,
        authorize: AuthJWT = Depends(get_auth_jwt_stub),
        service: AuthService = Depends(get_service_stub)
):
    """
    Вход пользователя и выдача токенов
    """
    return await service.login_user(data=data, authorize=authorize)


@auth_routers.get(
    path='/verify',
    responses={
        status.HTTP_200_OK: {'model': None},
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorResult[UserIdIsNotExists]
        }
    },
    response_model=None
)
async def token_verify(
        response: Response,
        authorize: AuthJWT = Depends(get_auth_jwt_stub),
        service: AuthService = Depends(get_service_stub),
):
    """
    Проверка токена
    """
    user_id = await service.verify_token(authorize=authorize)
    response.headers['X-User-ID'] = str(user_id)


@auth_routers.get(
    path='/refresh',
    responses={
        status.HTTP_200_OK: {'model': RefreshTokenResponse}
    },
    response_model=RefreshTokenResponse
)
async def token_refresh(
        authorize: AuthJWT = Depends(get_auth_jwt_stub),
        service: AuthService = Depends(get_service_stub),
):
    """
    Обновление токена
    """
    return await service.refresh_token(authorize=authorize)
