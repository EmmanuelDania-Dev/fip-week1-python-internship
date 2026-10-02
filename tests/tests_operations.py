import pytest

from calculator.errors import DivisionByZeroError
from calculator.operations import add, subtract, multiply, divide


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (2, 3, 5),
        (2.5, 1.5, 4.0),
        (-2, 3, 1),
        (0, 5, 5),
    ],
)
def test_add(left, right, expected):
    assert add(left, right) == expected


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (5, 3, 2),
        (3, 5, -2),
        (2.5, 1.5, 1.0),
        (-2, -3, 1),
    ],
)
def test_subtract(left, right, expected):
    assert subtract(left, right) == expected


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (2, 3, 6),
        (2.5, 4, 10.0),
        (-2, 3, -6),
        (0, 100, 0),
    ],
)
def test_multiply(left, right, expected):
    assert multiply(left, right) == expected


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (6, 3, 2),
        (5, 2, 2.5),
        (-6, 3, -2),
        (0, 5, 0),
    ],
)
def test_divide(left, right, expected):
    assert divide(left, right) == expected


def test_divide_by_zero():
    with pytest.raises(DivisionByZeroError, match="Cannot divide by zero."):
        divide(10, 0)
