"""This module contains a collection of helpers I frequently use."""
import csv
import json
from typing import List
from typing import Union


def read_json(filename: str) -> Union[dict, list]:
    """Read a JSON file.

    **Example**:

    >>> read_csv('/path/to/data.json')
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
