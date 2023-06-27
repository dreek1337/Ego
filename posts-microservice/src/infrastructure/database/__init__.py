from src.infrastructure.database.config import ElasticEngine
from src.infrastructure.database.main import elastic_factory

elastic_config = ElasticEngine()  # type: ignore
