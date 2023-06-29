from src.presentation import init_app
from src.presentation.api.config import APIConfig

app = init_app()
site_config = APIConfig()  # type: ignore
