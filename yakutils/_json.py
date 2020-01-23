"""This module contains boilerplate json helpers."""
import json
from typing import Iterator
from typing import Union


def read_json(filename: str) -> Union[dict, list]:
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


def iter_json(filename: str) -> Iterator[dict]:
    """Iterate a JSON file containing a list of dictionaries.

    **Example**:

    >>> for item in iter_json('/path/to/data.json'):
    ...     print(item)
    [{ 'name': 'foo' }]

    :param filename:
        Path to JSON file.
    :yield:
        A Python ``dict`` representation of a JSON object.
    """
    with open(filename) as fh:
        for item in json.loads(fh.read()):
            yield item
