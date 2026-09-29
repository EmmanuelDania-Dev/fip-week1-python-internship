from dataclasses import dataclass


@dataclass(frozen=True)
class Calculation:
    """Represents a single calculator operation."""

    left: float
    operator: str
    right: float
