import pytest

from calculator import Calculator, Calculation
from calculator.errors import UnsupportedOperatorError, DivisionByZeroError


@pytest.fixture
def calculator():
    return Calculator()


@pytest.mark.parametrize(
    ("left", "operator", "right", "expected"),
    [
        (2, "+", 3, 5),
        (5, "-", 2, 3),
        (4, "*", 3, 12),
        (10, "/", 2, 5),
    ],
)
def test_calculate(calculator, left, operator, right, expected):
    calculation = Calculation(left, operator, right)

    assert calculator.calculate(calculation) == expected


def test_calculate_unsupported_operator(calculator):
    calculation = Calculation(10, "%", 3)

    with pytest.raises(
        UnsupportedOperatorError,
        match=r"Unsupported operator: %",
    ):
        calculator.calculate(calculation)


def test_calculate_division_by_zero(calculator):
    calculation = Calculation(10, "/", 0)

    with pytest.raises(
        DivisionByZeroError,
        match="Cannot divide by zero.",
    ):
        calculator.calculate(calculation)


@pytest.mark.parametrize(
    ("method", "left", "right", "expected"),
    [
        ("add", 2, 3, 5),
        ("subtract", 5, 2, 3),
        ("multiply", 4, 3, 12),
        ("divide", 10, 2, 5),
    ],
)
def test_calculator_convenience_methods(
    calculator,
    method,
    left,
    right,
    expected,
):
    operation = getattr(calculator, method)

    assert operation(left, right) == expected


def test_add(calculator):
    assert calculator.add(2, 3) == 5


def test_subtract(calculator):
    assert calculator.subtract(5, 2) == 3


def test_multiply(calculator):
    assert calculator.multiply(4, 3) == 12


def test_divide(calculator):
    assert calculator.divide(10, 2) == 5


def test_divide_by_zero_through_calculator(calculator):
    with pytest.raises(DivisionByZeroError):
        calculator.divide(10, 0)
