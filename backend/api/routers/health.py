from fastapi import APIRouter

from api.schemas import HealthStatus, HealthVariables
from api.services import health_service

health_router = APIRouter(prefix="/health", tags=["health"])


@health_router.post("/check", response_model=HealthStatus)
async def check_health_endpoint(request: HealthVariables) -> HealthStatus:
    response: HealthStatus = health_service.check_health(
        weight=request.weight,
        height=request.height,
        systolic_bp=request.systolic_bp,
        diastolic_bp=request.diastolic_bp,
        glucose=request.glucose,
        heart_rate=request.heart_rate,
    )
    return response
