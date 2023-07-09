from fastapi import FastAPI
from src_users.presentation.api.controllers.avatar_routers import avatar_routers
from src_users.presentation.api.controllers.exceptions_handler import (
    setup_exception_handlers,
)
from src_users.presentation.api.controllers.healthcheck_router import (
    health_check_router,
)
from src_users.presentation.api.controllers.subscriptions_routers import (
    subscription_routers,
)
from src_users.presentation.api.controllers.users_routers import user_routers


def setup_controllers(app: FastAPI) -> None:
    app.include_router(health_check_router)
    setup_exception_handlers(app)
    app.include_router(user_routers)
    app.include_router(avatar_routers)
    app.include_router(subscription_routers)
