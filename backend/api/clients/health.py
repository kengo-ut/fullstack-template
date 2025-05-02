class HealthClient:
    """
    健康状態を管理するクライアントクラス。
    """

    def __init__(self):
        pass

    @staticmethod
    def calc_bmi(weight: float, height: float) -> float:
        """
        体重と身長からBMIを計算する。

        :param weight: 体重 (kg)
        :param height: 身長 (m)
        :return: BMI
        """
        return weight / (height**2)
