from dataclasses import FrozenInstanceError

import pytest

from calculator import Calculation


def test_calculation_stores_values():
    calculation = Calculation(10, "+", 5)

    assert calculation.left == 10
    assert calculation.operator == "+"
    assert calculation.right == 5


def test_calculation_is_frozen():
    calculation = Calculation(10, "+", 5)

    with pytest.raises(FrozenInstanceError):
        calculation.left = 20
