from polynomial import Polynomial
import pytest


def test_polynomial_ValueError_zero_value():
    coef = [(1, 5), (3, 0), (5, -1)]
    with pytest.raises(ValueError):
        Polynomial(coef)


def test_polynomial_ValueError_double():
    coef = [(1, 5), (3, 0), (5, -1)]
    with pytest.raises(ValueError):
        Polynomial(coef)


def test_polynomial_print_default_arg(capsys):
    print(Polynomial())
    captured = capsys.readouterr()
    assert captured.out == '0\n'


def test_polynomial_print_coef_minus_one(capsys):
    coef = [(1, 5), (0, 3), (5, -1)]
    print(Polynomial(coef))
    captured = capsys.readouterr()
    assert captured.out == '-x^5+5x+3\n'


def test_polynomial_print_no_coef(capsys):
    coef = [(1, -1), (5, 1)]
    print(Polynomial(coef))
    captured = capsys.readouterr()
    assert captured.out == 'x^5-x\n'


def test_polynomial_print_power_zero(capsys):
    print(Polynomial([(0, 1)]))
    captured = capsys.readouterr()
    assert captured.out == '1\n'


def test_polynomial_print_minus_one_at_power_0(capsys):
    coef = [(2, 1), (0, -1)]
    print(Polynomial(coef))
    captured = capsys.readouterr()
    assert captured.out == 'x^2-1\n'


def test_degree():
    coef = [(1, 5), (0, 3), (5, -1)]
    pol = Polynomial(coef)
    assert pol.degree() == 5


def test_coefficient():
    coef = [(0, 4), (1, -2)]
    pol = Polynomial(coef)
    assert pol.coefficient(1) == -2


def test_value1():
    coef = [(0, -8)]
    pol = Polynomial(coef)
    assert pol.value(3) == -8


def test_value2():
    coef = [(0, 4), (1, -2)]
    pol = Polynomial(coef)
    assert pol.value(1) == 2


def test_value3():
    coef = [(4, 2), (6, 3), (2, 3), (0, 7)]
    pol = Polynomial(coef)
    assert pol.value(2) == 243


def test_add_simple():
    pol1 = Polynomial([(2, 3)])
    pol2 = Polynomial([(2, 4)])
    pol3 = pol1 + pol2
    assert pol3.coefficient(2) == 7


def test_add_zero_coefficient():
    pol1 = Polynomial([(2, 3)])
    pol2 = Polynomial([(2, -3)])
    pol3 = pol1 + pol2
    assert pol3.coefficient(2) == None


def test_add():
    coef1 = [(4, 2), (6, 3), (2, 3), (0, 7)]
    pol1 = Polynomial(coef1)
    coef2 = [(4, -2), (6, 3), (0, 7), (5, 3)]
    pol2 = Polynomial(coef2)
    pol3 = pol1 + pol2
    assert 4 not in pol3._coefficients
    assert list(pol3._coefficients)[1] == 5
    assert pol3.coefficient(6) == 6
    assert pol3.coefficient(0) == 14
    assert pol3.coefficient(2) == 3


def test_subract_simple():
    pol1 = Polynomial([(1, 3)])
    pol2 = Polynomial([(1, 2)])
    pol3 = pol1 - pol2
    assert pol3.coefficient(1) == 1


def test_subtract():
    coef1 = [(4, 2), (6, 3), (2, 3), (0, 7)]
    pol1 = Polynomial(coef1)
    coef2 = [(4, -2), (6, 3), (0, 7), (5, 3)]
    pol2 = Polynomial(coef2)
    pol3 = pol1 - pol2
    assert 6 not in pol3._coefficients
    assert 0 not in pol3._coefficients
    assert pol3.coefficient(4) == 4
    assert pol3.coefficient(2) == 3
    assert pol3.coefficient(5) == -3
