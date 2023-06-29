from fastapi import FastAPI

from src.presentation.api import register_routers
from src.presentation.api.di import di_builder


def init_app() -> FastAPI:
    app = FastAPI()
    di_builder(app=app)
    register_routers(app=app)

    return app
