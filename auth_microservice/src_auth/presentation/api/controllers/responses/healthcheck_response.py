from pydantic import (
    BaseModel,
    Field,
)


class HealthCheckResponse(BaseModel):
    response: str = Field("OK", description="Ответ сервера")
