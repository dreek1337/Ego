from fastapi import FastAPI

from .controllers import (
    post_router,
    health_check_router,
    setup_exception_handlers
)


def register_routers(
        app: FastAPI
) -> None:
    app.include_router(health_check_router)
    app.include_router(post_router)
    setup_exception_handlers(app)
