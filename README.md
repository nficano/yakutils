# yakutils

Yakutils is a collection of helper methods I find myself often needing to write.  

This package is available on PyPi, but its primary purpose is to allow me to copy 
these into projects or to prevent me from needing to Google how to write them 
(I'm looking at you ``csv.DictReader`` and ``csv.DictWriter``).

As of this moment, ``yakutils`` has two methods, so needless to say its a long 
term work-in-progress.

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
