from fastapi import APIRouter, HTTPException

from api.lifespan import services
from api.schemas import HealthStatus, HealthVariables
from api.services import HealthService

health_router = APIRouter(prefix="/health", tags=["health"])


@health_router.post("/check", response_model=HealthStatus)
async def check_health_endpoint(request: HealthVariables) -> HealthStatus:
    health_service: HealthService = services["health_service"]
    try:
        response: HealthStatus = health_service.check_health(
            weight=request.weight,
            height=request.height,
            systolic_bp=request.systolic_bp,
            diastolic_bp=request.diastolic_bp,
            glucose=request.glucose,
            heart_rate=request.heart_rate,
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # noqa: B904
