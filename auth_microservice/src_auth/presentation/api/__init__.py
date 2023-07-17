from fastapi import FastAPI

from .controllers import (
    auth_routers,
    health_check_router,
)
from .controllers.excrptions_handler import setup_exception_handlers
from .middlewares import add_cors_middleware


def register_routers(app: FastAPI) -> None:
    app.include_router(health_check_router)
    app.include_router(auth_routers)
    setup_exception_handlers(app)
    add_cors_middleware(app)
