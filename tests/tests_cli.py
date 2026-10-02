import pytest

from calculator.cli import get_number, get_operator


def test_get_number_valid_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "42.5")

    assert get_number("Number: ") == 42.5


def test_get_number_retries_after_invalid_input(monkeypatch, capsys):
    inputs = iter(["abc", "10.5"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_number("Number: ")

    assert result == 10.5
    assert (
        "Invalid number.Please enter a valid number" in capsys.readouterr().out
        )


def test_get_operator_valid_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "+")

    assert get_operator() == "+"


@pytest.mark.parametrize("operator", ["+", "-", "*", "/"])
def test_get_operator_accepts_supported_operators(monkeypatch, operator):
    monkeypatch.setattr("builtins.input", lambda _: operator)

    assert get_operator() == operator


def test_get_operator_retries_after_invalid_input(monkeypatch, capsys):
    inputs = iter(["%", "invalid", "*"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_operator()

    assert result == "*"
    assert (
        "Invalid operation. Choose +, -, *, or /." in capsys.readouterr().out
        )
