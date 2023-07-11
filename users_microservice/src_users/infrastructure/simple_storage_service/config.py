from pydantic import (
    BaseSettings,
    Field,
    root_validator,
)


class MinioConfig(BaseSettings):
    host: str = Field("host", env="MINIO_HOST")
    port: str = Field("host", env="MINIO_PORT")
    aws_access_key_id: str = Field("access_key", env="MINIO_ROOT_PASSWORD")
    aws_secret_access_key: str = Field("secret_access_key", env="MINIO_ROOT_USER")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @root_validator
    def make_endpoint(cls, values):
        endpoint = "http://" + values.get("host") + ":" + values.get("port")
        values["endpoint_url"] = endpoint

        del values["host"]
        del values["port"]

        return values
