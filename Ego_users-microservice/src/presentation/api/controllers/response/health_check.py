from pydantic import (
    Field,
    BaseModel
)


class HealthCheckResponse(BaseModel):
    response: str = Field(..., description="Ответ сервера")
