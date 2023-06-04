from fastapi import FastAPI

from src.presentation.api.controllers.avatar_routers import avatar_routers
from src.presentation.api.controllers.users_routers import user_routers
from src.presentation.api.controllers.healthcheck_router import health_check_router
from src.presentation.api.controllers.exceptions_handler import setup_exception_handlers


def setup_controllers(
        app: FastAPI
) -> None:
    app.include_router(health_check_router)
    app.include_router(user_routers)
    app.include_router(avatar_routers)
    setup_exception_handlers(app)
