from typing import Literal

from api.clients import HealthClient
from api.schemas import HealthStatus


class HealthService:
    """
    健康状態を管理するサービスクラス。
    """

    def __init__(self):
        self.health_client = HealthClient()

    def check_health(
        self,
        weight: float,
        height: float,
        systolic_bp: int,
        diastolic_bp: int,
        glucose: int,
        heart_rate: int,
    ) -> HealthStatus:
        """
        入力された健康データを元に、健康状態を判定する。

        :param weight: 体重 (kg)
        :param height: 身長 (cm)
        :param systolic_bp: 収縮期血圧 (mmHg)
        :param diastolic_bp: 拡張期血圧 (mmHg)
        :param glucose: 血糖値 (mg/dL)
        :param heart_rate: 心拍数 (bpm)
        :return: HealthStatus 型の健康状態
        """

        bmi: float = self.health_client.calc_bmi(weight, height)

        # 健康基準の判定
        bmi_ok = 18.5 <= bmi <= 24.9
        bp_ok = systolic_bp <= 120 and diastolic_bp <= 80
        glucose_ok = 70 <= glucose <= 99
        heart_rate_ok = 60 <= heart_rate <= 100

        # 健康状態の判定
        status: Literal["健康", "注意", "危険"] = "健康"
        if all([bmi_ok, bp_ok, glucose_ok, heart_rate_ok]):
            status = "健康"
        elif any([not bmi_ok, not bp_ok, not glucose_ok, not heart_rate_ok]):
            status = "注意"
        else:
            status = "危険"
        return HealthStatus(status=status)


health_service = HealthService()
