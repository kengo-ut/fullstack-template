from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.clients import HealthClient
from api.services import HealthService

# Global variable to store services
services = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan function to handle startup and shutdown events."""
    # Startup event
    health_client = HealthClient()
    health_service = HealthService(health_client)
    services["health_service"] = health_service

    yield  # Server is running

    # Shutdown event
    services.clear()
