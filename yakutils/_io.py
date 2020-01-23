"""This module contains boilerplate io helpers."""
import csv
import json
from typing import Iterator
from typing import List
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


def read_csv(filename: str) -> List[dict]:
    """Read a CSV file.

    **Example**:

    >>> read_csv('/path/to/data.csv')
    [{ 'name': 'foo' }]

    :param filename:
        Path to CSV file.
    :return:
        A Python representation of the CSV document.
    """
    with open(filename) as fh:
        field_names = (
            fh.readline().replace('"', "").replace("\n", "").split(",")
        )
        dict_reader = csv.DictReader(fh, fieldnames=field_names)
        return list(dict(row) for row in dict_reader)


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


def iter_csv(filename: str) -> Iterator[dict]:
    """Iterate a CSV file.

    **Example**:

    >>> for item in iter_csv('/path/to/data.csv'):
    ...     print(item)
    [{ 'name': 'foo' }]

    :param filename:
        Path to CSV file.
    :yield:
        A Python ``dict`` representation of a CSV row.
    """
    with open(filename) as fh:
        field_names = (
            fh.readline().replace('"', "").replace("\n", "").split(",")
        )
        dict_reader = csv.DictReader(fh, fieldnames=field_names)
        for item in list(dict(row) for row in dict_reader):
            yield item
