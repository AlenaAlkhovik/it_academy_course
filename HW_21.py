import pytest

from practice_calculator import Calculator

@pytest.mark.parametrize('num1, num2, exp', [(7, 15, 22), (5, 14, 19)])
def test_add_positive_numbers(num1, num2, exp):
    assert Calculator().add(num1, num2) == exp

@pytest.mark.parametrize('num1, num2, exp', [(7, 0, 7), (0, 5, 5)])
def test_add_with_zero(num1, num2, exp):
    assert Calculator().add(num1, num2) == exp

@pytest.mark.parametrize('num1, num2, exp', [(-7, -15, -22), (4, -5, -1), (-100, 25, -75)])
def test_add_negative_numbers(num1, num2, exp):
    assert Calculator().add(num1, num2) == exp

@pytest.mark.parametrize('num1, num2, exp', [(0.7654, 78.7892, 79.5546), (18.14, 15.25, 33.39)])
def test_add_float_numbers(num1, num2, exp):
    assert Calculator().add(num1, num2) == pytest.approx(exp)

@pytest.mark.parametrize('num1, num2, exp', [(27, 9, 18), (114, 28, 86)])
def test_subtract_positive_numbers(num1, num2, exp):
    assert Calculator().subtract(num1, num2) == exp

@pytest.mark.parametrize('num1, num2, exp', [(4, 17, -13), (-100, 25, -125),(-100, -25, -75) ])
def test_subtract_negative_result(num1, num2, exp):
    assert Calculator().subtract(num1, num2) == exp

@pytest.mark.parametrize('num1, num2', [(4, 4), (-100, -100)])
def test_subtract_same_numbers(num1, num2):
    assert Calculator().subtract(num1, num2) == 0

@pytest.mark.parametrize('num1, num2, exp', [(4, 7, 28), (25, 4, 100)])
def test_multiply_positive_numbers(num1, num2, exp):
    assert Calculator().multiply(num1, num2) == exp

@pytest.mark.parametrize('num1, num2', [(0, 5), (1345, 0)])
def test_multiply_by_zero(num1, num2):
    assert Calculator().multiply(num1, num2) == 0

@pytest.mark.parametrize('num1, num2, exp', [(4, -7, -28), (-5, 12, -60), (-5, -27, 135)])
def test_multiply_negative_numbers(num1, num2, exp):
    assert Calculator().multiply(num1, num2) == exp

@pytest.mark.parametrize('num1, num2, exp', [(2.345, 7.973, 18.696685), (5.14, 12.87, 66.1518)])
def test_multiply_float_numbers(num1, num2, exp):
    assert Calculator().multiply(num1, num2) == pytest.approx(exp)

@pytest.mark.parametrize('num1, num2, exp', [(27, 9, 3), (840, 56, 15)])
def test_divide_positive_numbers(num1, num2, exp):
    assert Calculator().divide(num1, num2) == exp

@pytest.mark.parametrize('num1, num2, exp', [(-27, 9, -3), (-154, -2, 77), (144, -12, -12)])
def test_divide_negative_numbers(num1, num2, exp):
    assert Calculator().divide(num1, num2) == exp

@pytest.mark.parametrize('num1, num2', [(10, 2), (27, 9), (144, -12)])
def test_divide_result_is_float(num1, num2):
    number = Calculator().divide(num1, num2)
    assert isinstance(number, float)

@pytest.mark.parametrize('num1, num2, exp', [(7, 5, 16807), (12, 3, 1728)])
def test_power_positive_exponent(num1, num2, exp):
    assert Calculator().power(num1, num2) == exp

@pytest.mark.parametrize('num1, num2, exp', [(7, 0, 1), (13456, 0, 1)])
def test_power_zero_exponent(num1, num2, exp):
    assert Calculator().power(num1, num2) == exp

@pytest.mark.parametrize('num1, num2, exp', [(23, -2, 0.0018903591682), (5, -3, 0.008)])
def test_power_negative_exponent(num1, num2, exp):
    assert Calculator().power(num1, num2) == pytest.approx(exp)

@pytest.mark.parametrize('number, percent, exp', [(12596, 25, 3149), (1458, 27, 393.66)])
def test_percentage_positive_value(number, percent, exp):
    assert Calculator().percentage(number, percent) == pytest.approx(exp)

@pytest.mark.parametrize('number, percent, exp', [(12596, 0, 0), (1458, 0, 0)])
def test_percentage_zero_percent(number, percent, exp):
    assert Calculator().percentage(number, percent) == exp

@pytest.mark.parametrize('number, percent, exp', [(12596, 100, 12596), (1458, 100, 1458)])
def test_percentage_hundred_percent(number, percent, exp):
    assert Calculator().percentage(number, percent) == exp

def test_history_empty_by_default():
    assert Calculator().history == []

def test_history_after_add():
    calc = Calculator()
    calc.add(7,5)
    assert '7 + 5 = 12' in calc.history

def test_history_after_multiple_operations():
    calc = Calculator()
    calc.add(7,5)
    calc.subtract(10, 5)
    calc.divide(10, 5)
    calc.multiply(2, 3)
    calc.power(5, 2)
    calc.percentage(120, 20)
    expected = ['7 + 5 = 12', '10 - 5 = 5', '10 / 5 = 2.0', '2 * 3 = 6', '5 ** 2 = 25', '20% от 120 = 24.0']
    for item in expected:
        assert item in calc.history

def test_history_order():
    calc = Calculator()
    calc.add(7,5)
    calc.subtract(10, 5)
    calc.divide(10, 5)
    calc.multiply(2, 3)
    calc.power(5, 2)
    calc.percentage(120, 20)
    assert calc.history[0] == '7 + 5 = 12'
    assert calc.history[1] == '10 - 5 = 5'
    assert calc.history[2] == '10 / 5 = 2.0'
    assert calc.history[3] == '2 * 3 = 6'
    assert calc.history[4] == '5 ** 2 = 25'
    assert calc.history[5] == '20% от 120 = 24.0'

def test_clear_history():
    calc = Calculator()
    calc.add(7,5)
    calc.subtract(10, 5)
    calc.divide(10, 5)
    calc.multiply(2, 3)
    calc.power(5, 2)
    calc.clear_history()
    assert calc.history == []

def test_get_history_returns_copy():
    calc = Calculator()
    calc.add(7,5)
    calc.subtract(10, 5)
    calc.divide(10, 5)
    calc.multiply(2, 3)
    calc.power(5, 2)
    copied_history = calc.get_history()
    copied_history.append('1234567')
    assert '1234567' not in calc.history

def test_history_not_added_after_error():
    calc = Calculator()
    calc.add(7,5)
    with pytest.raises(ZeroDivisionError):
        calc.divide(100, 0)
    assert calc.history == ['7 + 5 = 12']

def test_divide_by_zero_error_message():
    with pytest.raises(ZeroDivisionError, match='Деление на ноль невозможно'):
        Calculator().divide(2345, 0)

def test_percentage_negative_error_message():
    with pytest.raises(ValueError, match='Процент не может быть отрицательным'):
        Calculator().percentage(23454, -23)

@pytest.mark.parametrize('num1, num2', [('sdf', 4), (5, 'ssd'), ('fdf', None), (3.5, [2, 5])])
def test_invalid_types_add(num1, num2):
    with pytest.raises(TypeError):
        Calculator().add(num1, num2)

@pytest.mark.parametrize('num1, num2', [('sdf', 4), (5, 'ssd'), ('fdf', None), (3.5, [2, 5])])
def test_invalid_types_divide(num1, num2):
    with pytest.raises(TypeError):
        Calculator().divide(num1, num2)