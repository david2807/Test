from calculator import Calculator

def test_add_two_positive():
    expected = 10
    result = Calculator.add(7, 3)
    assert result == expected

def test_subtract_two_positive():
    expected = 5
    result = Calculator.subtract(10, 5)
    assert result == expected

def test_divide():
    expected = 2
    result = Calculator.divide(10, 5)
    assert result == expected

def test_multiply():
    expected = 50
    result = Calculator.multiply(10, 5)
    assert result == expected