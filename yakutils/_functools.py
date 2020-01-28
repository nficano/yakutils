"""This module contains boilerplate functools helpers."""


def pipe(value, *funcs):
    """Pipe a value through a sequence of functions."""
    for func in funcs:
        value = func(value)
    return value
