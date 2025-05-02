import pytest
from fastapi import HTTPException

from api.schemas import HealthStatus
from api.services import HealthService


class MockHealthClient:
    def calc_bmi(self, weight: float, height: float) -> float:
        # シンプルな計算式で返す
        return weight / ((height / 100) ** 2)


@pytest.fixture
def service():
    return HealthService(health_client=MockHealthClient())


def test_health_status_healthy(service):
    result = service.check_health(
        weight=65,
        height=170,
        systolic_bp=115,
        diastolic_bp=75,
        glucose=90,
        heart_rate=70,
    )
    assert result == HealthStatus(status="健康")


def test_health_status_caution(service):
    result = service.check_health(
        weight=80,  # BMI高め
        height=170,
        systolic_bp=115,
        diastolic_bp=75,
        glucose=90,
        heart_rate=70,
    )
    assert result == HealthStatus(status="注意")


def test_health_status_danger(service):
    result = service.check_health(
        weight=90,  # BMI高め
        height=160,
        systolic_bp=140,  # 高血圧
        diastolic_bp=90,
        glucose=150,  # 高血糖
        heart_rate=110,  # 高心拍
    )
    assert result == HealthStatus(status="危険")


def test_invalid_height_raises_exception():
    class FailingClient:
        def calc_bmi(self, weight, height):
            raise ValueError("Height must be greater than 0")

    service = HealthService(health_client=FailingClient())

    with pytest.raises(HTTPException) as exc_info:
        service.check_health(
            weight=70,
            height=0,  # 無効値
            systolic_bp=120,
            diastolic_bp=80,
            glucose=90,
            heart_rate=70,
        )
    assert exc_info.value.status_code == 422
    assert "Height must be greater than 0" in str(exc_info.value.detail)
