from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    response: str = "OK"
