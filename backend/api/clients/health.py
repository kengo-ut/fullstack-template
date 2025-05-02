class HealthClient:
    """
    健康状態を管理するクライアントクラス。
    """

    def __init__(self):
        pass

    def calc_bmi(self, weight: float, height: float) -> float:
        """
        体重と身長からBMIを計算する。

        :param weight: 体重 (kg)
        :param height: 身長 (cm)
        :return: BMI
        """
        if height <= 0:
            raise ValueError("Height must be greater than 0")
        return weight / ((height / 100) ** 2)
