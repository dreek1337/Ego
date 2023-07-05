from fastapi import FastAPI

from .controllers import auth_routers, health_check_router, user_routers
from .controllers.excrptions_handler import setup_exception_handlers


def register_routers(
        app: FastAPI
) -> None:
    app.include_router(health_check_router)
    app.include_router(auth_routers)
    app.include_router(user_routers)
    setup_exception_handlers(app)
