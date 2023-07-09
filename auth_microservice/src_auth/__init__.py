from src_auth.config.settings.site_config import APIConfig
from src_auth.presentation import init_app

app = init_app()
site_config = APIConfig().dict()  # type: ignore
