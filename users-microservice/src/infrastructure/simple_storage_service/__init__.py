from src.infrastructure.simple_storage_service.config import MinioConfig
from src.infrastructure.simple_storage_service.main import s3_factory
from src.infrastructure.simple_storage_service.minio import \
    UserCloudStorageImpl

cloud_config = MinioConfig()  # type: ignore
