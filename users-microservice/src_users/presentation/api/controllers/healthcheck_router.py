from fastapi import APIRouter, status
from src_users.presentation.api.controllers.response import HealthCheckResponse

health_check_router = APIRouter(tags=["health_check"])


@health_check_router.get(
    path="/", status_code=status.HTTP_200_OK, response_model=HealthCheckResponse
)
async def health_check():
    return HealthCheckResponse(response="OK")
