from fastapi import FastAPI
from src_users.presentation.api.config import APIConfig
from src_users.presentation.api.controllers import setup_controllers
from src_users.presentation.api.di import setup_di


def init_app() -> FastAPI:
    app = FastAPI()
    setup_di(app=app)
    setup_controllers(app=app)

    return app
