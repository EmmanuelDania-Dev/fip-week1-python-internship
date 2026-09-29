def add(left, right):
    return left + right


def subtract(left, right):
    return left - right


def multiply(left, right):
    return left * right


def divide(left, right):
    if right == 0:
        print("Error: Cannot divide by zero.")
        return None

    return left / right


def get_number(prompt):
    while True:
        value = input(prompt)

        try:
            return float(value)
        except ValueError:
            print("Invalid number. Please enter a valid number.")


def get_operator():
    while True:
        operator = input("Enter operation (+, -, *, /): ")

        if operator in ["+", "-", "*", "/"]:
            return operator

        print("Invalid operation. Choose +, -, *, or /.")


def calculate(left, operator, right):
    if operator == "+":
        return add(left, right)

    if operator == "-":
        return subtract(left, right)

    if operator == "*":
        return multiply(left, right)

    if operator == "/":
        return divide(left, right)


def main():
    print("Calculator")
    print("Enter two numbers and an operation.")
    print("Type Ctrl+C to exit.")

    try:
        while True:
            print()

            left = get_number("First number: ")
            operator = get_operator()
            right = get_number("Second number: ")

            result = calculate(left, operator, right)

            if result is not None:
                print(f"Result: {result}")

    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
