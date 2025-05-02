import pytest

from api.clients import HealthClient


@pytest.mark.parametrize(
    "weight, height, expected_bmi",
    [
        (70, 175, 22.86),
        (60, 160, 23.44),
        (80, 180, 24.69),
        (50, 150, 22.22),
    ],
)
def test_calc_bmi_parametrized(weight, height, expected_bmi):
    client = HealthClient()
    bmi = client.calc_bmi(weight, height)
    assert round(bmi, 2) == expected_bmi
