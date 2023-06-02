from fastapi import FastAPI

from src.presentation.api.controllers.users_routers import users_router
from src.presentation.api.controllers.healthcheck_router import health_check_router
from src.presentation.api.controllers.exceptions_handler import setup_exception_handlers


def setup_controllers(
        app: FastAPI
) -> None:
    app.include_router(health_check_router)
    app.include_router(users_router)
    setup_exception_handlers(app)
