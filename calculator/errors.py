class CalculatorError(Exception):
    """Base exception for calculator errors."""


class UnsupportedOperatorError(CalculatorError):
    """Raised when an unsupported operator is requested."""

    def __init__(self, operator: str) -> None:
        super().__init__(f"Unsupported operator: {operator}")


class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""

    def __init__(self) -> None:
        super().__init__("Cannot divide by zero.")
