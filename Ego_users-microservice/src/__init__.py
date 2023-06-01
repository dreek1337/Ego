from src.presentation.api import (
    init_app,
    APIConfig
)

app = init_app()  # type: ignore
app_config = APIConfig().dict()  # type: ignore
