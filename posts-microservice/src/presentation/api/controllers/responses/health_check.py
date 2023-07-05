from pydantic import BaseModel, Field


class HealthCheckResponse(BaseModel):
    response: str = Field(..., description="Ответ сервера")
