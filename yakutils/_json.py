"""This module contains boilerplate json helpers."""
import datetime as dt
import json
from decimal import Decimal

from ._datetime import date_to_iso8601
from ._datetime import datetime_to_iso8601

__all__ = ["JSONEncoder", "read_json", "iter_json"]


class JSONEncoder(json.JSONEncoder):
    """Extend JSONEncoder to gracefully handle various primitives."""

    def default(self, o):
        """Convert data into a serializable format."""
        if isinstance(o, dt.datetime):
            return datetime_to_iso8601(o)
        elif isinstance(o, dt.date):
            return date_to_iso8601(o)
        elif isinstance(o, dt.time):
            representation = o.isoformat()
            if o.microsecond:
                return representation[:12]
            return representation
        elif isinstance(o, Decimal):
            return float(o)
        elif hasattr(o, "__getitem__"):
            return dict(o)
        elif hasattr(o, "__iter__"):
            return tuple(item for item in o)
        return super(JSONEncoder, self).default(o)


def read_json(filename):
    """Read a JSON file.

    **Example**:

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

    **Example**:

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
