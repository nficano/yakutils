"""This module contains boilerplate random helpers."""
import random
from string import ascii_letters
from string import digits

__all__ = ["random_string", "random_tolerance"]


def random_string(n):
    """Generate a random alphanumeric string of size ``n``."""
    return "".join(random.choices(ascii_letters + digits, k=n))


def random_tolerance(value, tolerance):
    """Generate a value within a small tolerance.

    Credit: /u/LightShadow on Reddit.

    Example::
        >>> time.sleep(random_tolerance(1.0, 0.01))
        >>> a = random_tolerance(4.0, 0.25)
        >>> assert 3.0 <= a <= 5.0
        True
    """
    value = float(value)
    if tolerance == 0.0:
        return value
    return value + value * random.uniform(-tolerance, tolerance)
