from typing import Protocol


class HealthClientProtocol(Protocol):
    """
    HealthClientのインターフェースを定義するProtocol。
    これを満たすクラスなら依存注入可能。
    """

    def calc_bmi(self, weight: float, height: float) -> float:
        """
        体重と身長からBMIを計算する。

        :param weight: 体重 (kg)
        :param height: 身長 (cm)
        :return: BMI
        """
        ...
