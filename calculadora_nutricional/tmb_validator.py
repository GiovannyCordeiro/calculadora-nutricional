class TMBValidator:

    @staticmethod
    def validate_ints(*args):
        for value in args:
            if not isinstance(value, int):
                raise TypeError(f"O valor '{value}' deve ser um inteiro.")
