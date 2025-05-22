from .tmb_validator import TMBValidator


class TMB:
    def __init__(self, weight: int, height: int, age: int):
        TMBValidator.validate_ints(weight, height, age)
        self.weight = weight
        self.height = height
        self.age = age

    def calc(self, gender):
        if gender is None:
            raise ValueError('A variavel gender tem que ser'
            ' atribuido um valor female ou male')

        if gender == 'female' or gender == 'f':
            return self.female_calc()
        return self.male_calc()

    def female_calc(self) -> int:
        result = 447.593 + (9.247 * float(self.weight)) \
            + (3.098 * float(self.height)) - (4.330 * float(self.age))
        return round(result)

    def male_calc(self) -> int:
        result = 88.362 + (13.397 * float(self.weight)) \
            + (4.799 * float(self.height)) - (5.677 * float(self.age))
        return round(result)
