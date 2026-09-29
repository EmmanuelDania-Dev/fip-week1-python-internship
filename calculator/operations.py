from collections.abc import Callable
from .errors import DivisionByZeroError

Operation = Callable[[float, float], float]


def add(left: float, right: float) -> float:
    """Return the sum of two numbers."""
    return left + right


def subtract(left: float, right: float) -> float:
    """Return the difference of two numbers."""
    return left - right


def multiply(left: float, right: float) -> float:
    """Return the product of two numbers."""
    return left * right


def divide(left: float, right: float) -> float:
    """Return the quotient of two numbers."""
    if right == 0:
        raise DivisionByZeroError()

    return left / right


OPERATIONS: dict[str, Operation] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
