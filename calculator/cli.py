from .calculator import Calculator
from .errors import CalculatorError
from .models import Calculation


def get_number(prompt: str) -> float:
    """Read a floating-point number from the user."""
    while True:
        value = input(prompt).strip()

        try:
            return float(value)
        except ValueError:
            print("Invalid number. Please enter a valid number.")


def get_operator() -> str:
    """Read a supported arithmetic operator from the user."""
    operators = {"+", "-", "*", "/"}

    while True:
        operator = input("Enter operation (+, -, *, /): ").strip()

        if operator in operators:
            return operator

        print("Invalid operation. Choose +, -, *, or /.")


def run() -> None:
    """Run the calculator command-line interface."""
    calculator = Calculator()

    print("Calculator")
    print("Enter two numbers and an operation.")
    print("Type Ctrl+C to exit.")

    try:
        while True:
            print()

            left = get_number("First number: ")
            operator = get_operator()
            right = get_number("Second number: ")

            calculation = Calculation(left, operator, right)

            try:
                result = calculator.calculate(calculation)
                print(f"Result: {result}")
            except CalculatorError as error:
                print(f"Error: {error}")

    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    run()
