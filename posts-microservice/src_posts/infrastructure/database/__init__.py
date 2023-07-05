from src_posts.infrastructure.database.config import ElasticEngine
from src_posts.infrastructure.database.main import elastic_factory
from src_posts.infrastructure.database.repositories import *
from src_posts.infrastructure.database.uow import ElasticsearchUoW

elastic_config = ElasticEngine()  # type: ignore
