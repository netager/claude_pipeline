import math


def add(a: int | float, b: int | float) -> int | float:
    return a + b


def divide(a: int | float, b: int | float) -> float:
    if not isinstance(a, (int, float)):
        raise TypeError(f"'a' must be int or float, got {type(a).__name__!r}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"'b' must be int or float, got {type(b).__name__!r}")
    if b == 0:
        raise ValueError(f"Cannot divide by zero: b={b!r}")
    if not math.isfinite(b):
        raise ValueError(f"Divisor must be a finite number, got b={b!r}")
    return a / b
