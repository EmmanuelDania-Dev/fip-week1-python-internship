# CLI Calculator

A simple command-line calculator built with Python.

The calculator supports the four basic arithmetic operations:

- Addition (+)

- Subtraction (-)

- Multiplication (*)

- Division (/)

It also includes custom exceptions for unsupported operations and division by zero.

## Demo Video
## Demo

[Watch the Week 1 calculator demo]([text](https://drive.google.com/file/d/1S3UC7CnhVrUD10aKQhDZOtHX9UhSunw4/view?usp=sharing))

- Interactive command-line interface

- Addition, subtraction, multiplication, and division

- Input validation for numbers

- Input validation for operators

- Handles division by zero

- Custom calculator exceptions

- Uses Python dataclasses to represent calculations

- Clean separation between the CLI, calculator logic, operations, models, and errors

## Project Structure

calculator-project/
└── calculator/
    ├── __init__.py
    ├── calculator.py
    ├── cli.py
    ├── errors.py
    ├── models.py
    └── operations.py

## Files

 - cli.py — Handles user interaction through the terminal.

- calculator.py — Contains the main Calculator class.

- operations.py — Contains the arithmetic operations.

- models.py — Defines the Calculation dataclass.

- errors.py — Defines custom calculator exceptions.

- __init__.py — Exposes the main package classes and exceptions.

## Requirements

Python 3.10 or newer

No external Python packages are required.

 - Installation

Clone or download the project, then open a terminal in the directory containing the calculator folder.

**For example:**

calculator-project/
└── calculator/
    ├── __init__.py
    ├── calculator.py
    ├── cli.py
    ├── errors.py
    ├── models.py
    └── operations.py


**You can verify that Python is installed with:**

python --version


**On some systems, use:**

python3 --version

**Running the Calculator**

From the directory containing the calculator package, run:

python -m calculator.cli


**If your system uses python3, run:**

python3 -m calculator.cli


You should see:

Calculator
Enter two numbers and an operation.
Type Ctrl+C to exit.

**Usage**

The calculator will ask you for two numbers and an operation.

Example:

Calculator
Enter two numbers and an operation.
Type Ctrl+C to exit.

First number: 10
Enter operation (+, -, *, /): *
Second number: 5
Result: 50.0

**Addition**
First number: 10
Enter operation (+, -, *, /): +
Second number: 5
Result: 15.0

**Subtraction**
First number: 10
Enter operation (+, -, *, /): -
Second number: 5
Result: 5.0

**Multiplication**
First number: 10
Enter operation (+, -, *, /): *
Second number: 5
Result: 50.0

**Division**
First number: 10
Enter operation (+, -, *, /): /
Second number: 5
Result: 2.0

**Error Handling**

The calculator validates user input and handles common errors.

Invalid number

If you enter something that isn't a valid number:

First number: hello
Invalid number. Please enter a valid number.


The calculator will ask you to enter the number again.

Invalid operation

Only these operations are supported:

## +
## -
## *
## /


For example:

Enter operation (+, -, *, /): %
Invalid operation. Choose +, -, *, or /.

**Division by zero**

The calculator prevents division by zero:

First number: 10
Enter operation (+, -, *, /): /
Second number: 0
Error: Cannot divide by zero.

**Exiting**

To exit the calculator, press:

Ctrl+C


The program will display:

Goodbye!

## Example Session

Calculator
Enter two numbers and an operation.
Type Ctrl+C to exit.

First number: 25
Enter operation (+, -, *, /): /
Second number: 5
Result: 5.0

First number: 8
Enter operation (+, -, *, /): *
Second number: 7
Result: 56.0

First number: 10
Enter operation (+, -, *, /): /
Second number: 0
Error: Cannot divide by zero.

First number: 12
Enter operation (+, -, *, /): +
Second number: 8
Result: 20.0

## Architecture

The project separates responsibilities into different modules.

User
 │
 ▼
cli.py
 │
 ▼
Calculator
 │
 ▼
operations.py
 │
 ▼
Result


The cli.py module is responsible for collecting input and displaying results.

The Calculator class in calculator.py receives a Calculation object and determines which operation should be performed.

The arithmetic functions are stored in the OPERATIONS dictionary in operations.py.

Custom errors are defined in errors.py and used when something goes wrong.

## License

This project is available for educational and personal use.
