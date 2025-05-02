from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_health():
    response = client.post(
        "/api/health/check",
        json={
            "weight": 70,
            "height": 175,
            "systolic_bp": 118,
            "diastolic_bp": 78,
            "glucose": 90,
            "heart_rate": 75,
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "status": "注意",
    }
