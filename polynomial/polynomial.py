class Polynomial:
    def __init__(self, coefficients: list = []):
        _coefficients = list(reversed(sorted(coefficients)))
        self._validate_arguments(coefficients)
        self._coefficients = {}
        for cof in _coefficients:
            self._coefficients[cof[0]] = cof[1]

    def __str__(self):
        text = ""
        for power, coef in self._coefficients.items():
            if text and coef > 0:
                text += '+'
            if power != 0:
                text += '-' if coef == \
                    -1 else '' if coef == 1 else str(coef)
                text += 'x' if power == 1 else 'x^' + str(power)
            else:
                text += str(coef)
        return text if text != '' else '0'

    def _validate_arguments(self, coefficients: list):
        powers = []
        for cof in coefficients:
            if cof[0] < 0 or cof[1] == 0 or cof[0] in powers or not isinstance(cof[1], int):
                raise ValueError
            powers.append(cof[0])

    def degree(self):
        return list(self._coefficients)[0]

    def coefficient(self, power):
        try:
            return self._coefficients[power]
        except(KeyError):
            return None

    def value(self, x):
        value = 0
        for key in self._coefficients:
            value += self._coefficients[key] * (x ** key)
        return value

    def __add__(self, other):
        set_of_powers = set(self._coefficients.keys()).union(
            set(other._coefficients.keys()))
        _sum_coefficients = []
        for power in set_of_powers:
            new_coef = self._coefficients.get(
                power, 0) + other._coefficients.get(
                power, 0)
            if new_coef != 0:
                _sum_coefficients.append((power, new_coef))
        return Polynomial(_sum_coefficients)

    def __sub__(self, other):
        negated = {}
        for power in other._coefficients:
            negated[power] = -other._coefficients[power]
        return self + Polynomial(list(negated.items()))


if __name__ == "__main__":
    print(Polynomial([(1, 5), (3, 2), (5, -1), (0, -3)]))
