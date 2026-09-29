from .errors import UnsupportedOperatorError
from .models import Calculation
from .operations import OPERATIONS


class Calculator:
    """Perform arithmetic calculations."""

    def calculate(self, calculation: Calculation) -> float:
        """Evaluate a calculation and return its result."""
        operation = OPERATIONS.get(calculation.operator)

        if operation is None:
            raise UnsupportedOperatorError(calculation.operator)

        return operation(calculation.left, calculation.right)

    def add(self, left: float, right: float) -> float:
        """Add two numbers."""
        return self.calculate(Calculation(left, "+", right))

    def subtract(self, left: float, right: float) -> float:
        """Subtract two numbers."""
        return self.calculate(Calculation(left, "-", right))

    def multiply(self, left: float, right: float) -> float:
        """Multiply two numbers."""
        return self.calculate(Calculation(left, "*", right))

    def divide(self, left: float, right: float) -> float:
        """Divide two numbers."""
        return self.calculate(Calculation(left, "/", right))
