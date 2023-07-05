from pydantic import BaseSettings, Field, root_validator


class ElasticEngine(BaseSettings):
    port: int = Field(..., env='ELASTIC_PORT')
    host: str = Field(..., env='ELASTIC_HOST')
    password: str = Field(..., env='ELASTIC_PASSWORD')
    username: str = Field(..., env='ELASTIC_USERNAME')

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @root_validator
    def create_es_connection(cls, values) -> dict:
        port = values.get('port')
        host = values.get('host')
        password = values.get('password')
        username = values.get('username')

        es_settings = dict()

        es_settings['hosts'] = f'http://{host}:{port}'
        es_settings['http_auth'] = (username, password)  # type: ignore

        return es_settings
