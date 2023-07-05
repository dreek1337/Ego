from src_users.presentation.api import APIConfig, init_app

app = init_app()  # type: ignore
app_config = APIConfig().dict()  # type: ignore
