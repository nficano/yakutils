<div align="center">
  <p>
    <img src="https://assets.nickficano.com/gh-yakutils.min.svg" width="270" height="135" alt="yakutils logo" />
  </p>
<p align="center">
  <img src="https://img.shields.io/pypi/v/yakutils.svg" alt="pypi">
  <a href="https://pypi.org/project/yakutils/">
    <img src="https://img.shields.io/pypi/dm/yakutils.svg" alt="pypi">
  </a>
  <a href="https://pypi.python.org/pypi/yakutils/">
    <img src="https://img.shields.io/pypi/pyversions/yakutils.svg" />
  </a>
</p>
</div>

# yakutils

Yakutils is a collection of helper methods I find myself often needing to write.

This package is available on PyPi, but its primary purpose is to allow me to copy
these into projects or to prevent me from needing to Google how to write them
(I'm looking at you ``csv.DictReader`` and ``csv.DictWriter``).

As of this moment, ``yakutils`` is little more than a project placeholder,
what with having two methods. So needless to say, it's a long term work-in-progress.

## Installation

To download using pip via PyPi:

```bash
$ pip install yakutils
```

## Usage:

```python
>>> from yakutils import read_csv
>>> read_csv('/path/to/data.csv')
[
  {
    'name': 'Tomatillo',
    'age': 27
  },
  # ...
]
>>> from yakutils import read_json
>>> read_csv('/path/to/data.json')
[
  {
    'name': 'Tomatillo',
    'age': 27
  },
  # ...
]
```
