from src_posts.presentation import init_app
from src_posts.presentation.api.config import APIConfig

app = init_app()
site_config = APIConfig()  # type: ignore
