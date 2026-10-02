from calculator.errors import (
    CalculatorError,
    DivisionByZeroError,
    UnsupportedOperatorError,
)


def test_calculator_error_is_base_exception():
    error = CalculatorError()

    assert isinstance(error, Exception)


def test_unsupported_operator_error_message():
    error = UnsupportedOperatorError("%")

    assert str(error) == "Unsupported operator: %"


def test_unsupported_operator_error_inherits_calculator_error():
    error = UnsupportedOperatorError("%")

    assert isinstance(error, CalculatorError)


def test_division_by_zero_error_message():
    error = DivisionByZeroError()

    assert str(error) == "Cannot divide by zero."


def test_division_by_zero_error_inherits_calculator_error():
    error = DivisionByZeroError()

    assert isinstance(error, CalculatorError)
