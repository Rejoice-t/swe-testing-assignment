import pytest
from quick_calc.calculator import add, subtract, multiply, divide


def test_add():
    assert add(5, 3) == 8


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(6, 7) == 42


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)


def test_negative_numbers():
    assert add(-5, -3) == -8


def test_decimal_numbers():
    assert multiply(2.5, 2) == 5.0


def test_large_numbers():
    assert add(1_000_000, 2_000_000) == 3_000_000