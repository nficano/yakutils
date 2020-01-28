"""This module contains boilerplate json helpers."""
import datetime as dt
import json
from decimal import Decimal
from functools import singledispatch

from ._datetime import date_to_iso8601
from ._datetime import datetime_to_iso8601

__all__ = ["json_defaults", "read_json", "iter_json"]


def read_json(filename):
    """Read a JSON file.

    Example::
        >>> read_json('/path/to/data.json')
        [{ 'name': 'foo' }]

    :param filename:
        Path to JSON file.
    :return:
        A Python representation of the JSON document.
    """
    with open(filename) as fh:
        return json.loads(fh.read())


def iter_json(filename):
    """Iterate a JSON file containing a list of dictionaries.

    Example::
        >>> for item in iter_json('/path/to/data.json'):
        ...    print(item)
    [{ 'name': 'foo' }]

    :param filename:
        Path to JSON file.
    :yield:
        A Python ``dict`` representation of a JSON object.
    """
    with open(filename) as fh:
        for item in json.loads(fh.read()):
            yield item


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
