"""This module contains boilerplate random helpers."""
import random
from string import ascii_letters
from string import digits

__all__ = ["random_string"]


def random_string(n):
    """Generate a random alphanumeric string of size ``n``."""
    symbols = ascii_letters + digits
    return "".join(random.choice(symbols) for i in range(n))
