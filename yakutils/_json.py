"""This module contains boilerplate json helpers."""
import datetime as dt
import json
import pathlib
from decimal import Decimal
from functools import singledispatch
from typing import Union

from ._datetime import date_to_iso8601
from ._datetime import datetime_to_iso8601

__all__ = ["json_defaults", "read_json"]


def read_json(filename: Union[pathlib.Path, str]):
    """Read a JSON file.

    Example::
        >>> read_json('/path/to/data.json')
        [{ 'name': 'foo' }]

    :param filename:
        Path to JSON file.
    :return:
        A Python representation of the JSON document.
    """
    if isinstance(filename, str):
        filename = pathlib.Path(filename)
    with open(filename) as fh:
        return json.loads(fh.read())


@singledispatch
def json_defaults(val):
    """Create a generic JSON encodable value."""
    return str(val)


@json_defaults.register(dt.datetime)
def _serialize_datetime(val):
    """Create a JSON encodable value of a datetime object."""
    return datetime_to_iso8601(val)


@json_defaults.register(dt.date)
def _serialize_date(val):
    """Create a JSON encodable value of a date object."""
    return date_to_iso8601(val)


@json_defaults.register(dt.date)
def _serialize_time(val):
    """Create a JSON encodable value of a time object."""
    return val.isoformat()


@json_defaults.register(Decimal)
def _serialize_decimal(val):
    """Create a JSON encodable value of a Decimal object."""
    return float(val)
