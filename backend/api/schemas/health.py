from typing import Literal

from pydantic import BaseModel, Field


class HealthStatus(BaseModel):
    status: Literal["健康", "注意", "危険"] = Field(
        examples=["健康", "注意", "危険"], description="健康状態"
    )


class HealthVariables(BaseModel):
    weight: float = Field(..., description="体重 (kg)")
    height: float = Field(..., description="身長 (m)")
    systolic_bp: int = Field(..., description="収縮期血圧 (mmHg)")
    diastolic_bp: int = Field(..., description="拡張期血圧 (mmHg)")
    glucose: int = Field(..., description="血糖値 (mg/dL)")
    heart_rate: int = Field(..., description="心拍数 (bpm)")

    # example values
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "weight": 70.0,
                    "height": 1.75,
                    "systolic_bp": 120,
                    "diastolic_bp": 80,
                    "glucose": 90,
                    "heart_rate": 70,
                },
            ]
        }
    }
