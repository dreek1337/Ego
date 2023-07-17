from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def add_cors_middleware(app: FastAPI) -> None:
    origins = [
        "http://swagger.ui",
        "http://swagger.ui:8002",
        "http://0.0.0.0",
        "http://0.0.0.0:8002",
        "http://84.252.141.163",
        "http://84.252.141.163:8002",
    ]

    return app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
