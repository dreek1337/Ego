from fastapi import FastAPI

from src.presentation.api.di import setup_di
from src.presentation.api.controllers import setup_controllers


def init_app() -> FastAPI:
    app = FastAPI()
    setup_di(app=app)
    setup_controllers(app=app)

    return app
