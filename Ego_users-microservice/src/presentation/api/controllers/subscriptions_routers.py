from fastapi import (
    status,
    Depends,
    APIRouter
)

from src import application as app
from src.presentation.api.di import get_service_stub
from src.presentation.api.controllers import response as resp
from src.application.user.service.user_service import UserService
from .request.subscription_requests import (
    SubscribeRequest,
    UnubscribeRequest,
    GetSubscribersRequest,
    GetSubscriptionsRequest
)
from .response.subscription_response import (
    SubscribeResponse,
    UnsubscribeResponse,
    SubscribersResponse,
    SubscriptionsResponse
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
            'model': resp.ErrorResult[app.SubscribeOnYourself]
        },
        status.HTTP_404_NOT_FOUND: {
            'model': resp.ErrorResult[app.UserIsNotExist]
        },
        status.HTTP_409_CONFLICT: {
            'model': resp.ErrorResult[app.SubscribeIsAlreadyExists]
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
            'model': resp.ErrorResult[app.SubscribeIsNotExists]
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


@subscription_routers.get(
    path='/get_subscriptions',
    responses={
        status.HTTP_200_OK: {'model': SubscriptionsResponse},
        status.HTTP_404_NOT_FOUND: {
            'model': resp.ErrorResult[app.UserIsNotExist]
        }
    },
    response_model=SubscriptionsResponse
)
async def get_subscriptions(
        subscriptions_data: GetSubscriptionsRequest = Depends(),
        service: UserService = Depends(get_service_stub)
):
    """
    Получение подписчиков пользователя
    """
    return await service.get_subscriptions(data=subscriptions_data)


@subscription_routers.get(
    path='/get_subscribers',
    responses={
        status.HTTP_200_OK: {'model': SubscribersResponse},
        status.HTTP_404_NOT_FOUND: {
            'model': resp.ErrorResult[app.UserIsNotExist]
        }
    },
    response_model=SubscribersResponse
)
async def get_subscribers(
        subscribers_data: GetSubscribersRequest = Depends(),
        service: UserService = Depends(get_service_stub)
):
    """
    Получение подписчиков пользователя
    """
    return await service.get_subscribers(data=subscribers_data)
