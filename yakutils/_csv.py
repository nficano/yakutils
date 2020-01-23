"""This module contains boilerplate csv helpers."""
import csv
from typing import Iterator
from typing import List


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
