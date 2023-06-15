from fastapi import (
    status,
    Depends,
    Response,
    APIRouter
)
from fastapi_jwt_auth import AuthJWT  # type: ignore


from src.application import AuthService
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
    RegistrationResponse,
    RefreshTokenResponse
)

auth_routers = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@auth_routers.post(
    path='/registration',
    responses={
      status.HTTP_200_OK: {'model': RegistrationResponse}
    },
    response_model=RegistrationResponse
)
async def user_registration(
        data: RegistrationRequest,
        service: AuthService = Depends(get_service_stub)
):
    """
    Регистрация пользователя
    """
    return await service.registration_user(data=data)


@auth_routers.post(
    path='/login',
    responses={
      status.HTTP_200_OK: {'model': TokensResponse}
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
        status.HTTP_200_OK: {'model': None}
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
