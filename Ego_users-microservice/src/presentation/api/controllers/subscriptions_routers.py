from fastapi import (
    status,
    Depends,
    APIRouter
)

from src.presentation.api.di import get_service_stub
from src.presentation.api.controllers import response as resp
from src.application.user.service.user_service import UserService
from src.application import (
    SubscribeOnYourself,
    SubscribeIsNotExists,
    SubscribeIsAlreadyExists,
    UserForSubscribeIsNotExists
)
from .request.subscription_requests import (
    SubscribeRequest,
    UnubscribeRequest
)
from .response.subscription_response import (
    SubscribeResponse,
    UnsubscribeResponse
)

subscription_routers = APIRouter(
    tags=['subscription'],
    prefix='/subscription'
)


@subscription_routers.post(
    path='/subscribe',
    responses={
        status.HTTP_201_CREATED: {'model': SubscribeResponse},
        status.HTTP_400_BAD_REQUEST: {
            'model': resp.ErrorResult[SubscribeOnYourself]
        },
        status.HTTP_404_NOT_FOUND: {
            'model': resp.ErrorResult[UserForSubscribeIsNotExists]
        },
        status.HTTP_409_CONFLICT: {
            'model': resp.ErrorResult[SubscribeIsAlreadyExists]
        }
    },
    response_model=SubscribeResponse
)
async def subscribe(
        subscribe_data: SubscribeRequest,
        service: UserService = Depends(get_service_stub)
):
    """
    Оформление подписки
    """
    return await service.subscribe(data=subscribe_data)


@subscription_routers.post(
    path='/unsubscribe',
    responses={
        status.HTTP_200_OK: {'model': UnsubscribeResponse},
        status.HTTP_404_NOT_FOUND: {
            'model': resp.ErrorResult[SubscribeIsNotExists]
        }
    },
    response_model=UnsubscribeResponse
)
async def unsubscribe(
        unsubscribe_data: UnubscribeRequest,
        service: UserService = Depends(get_service_stub)
):
    """
    Отписка от пользователя
    """
    return await service.unsubscribe(data=unsubscribe_data)
