from src.infrastructure.database.repositories import *
from src.infrastructure.database.config import ElasticEngine
from src.infrastructure.database.main import elastic_factory
from src.infrastructure.database.uow import ElasticsearchUoW

elastic_config = ElasticEngine()  # type: ignore
