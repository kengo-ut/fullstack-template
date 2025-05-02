from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import health_router

app = FastAPI(
    title="Health API",
    version="1.0.0",
    description="Health API for monitoring health metrics",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)

app.include_router(health_router, prefix="/api")
