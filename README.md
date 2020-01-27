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

Yak-utils is yet another toolbox of Python helper functions.

This package is available on PyPi, but its primary purpose is to allow one (me) to copy these into projects or to prevent one (me as well) from needing to Google how to write them (I'm looking at you ``csv.DictReader`` and ``csv.DictWriter``).

This project is a continuous work-in-progress, and while its contents are specific to stuff that I use, pull requests are certainly welcome.

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

>>> from yakutils import iter_csv
>>> for item in yakutils.iter_csv('/path/to/data.csv'):
...   print(item)
[
  {
    'name': 'Tomatillo',
    'age': 27
  },
  # ...
]

>>> import datetime as dt
>>> from yakutils import date_to_iso8601
>>> date_to_iso8601(dt.date.today())
'2020-01-26T00:00:00Z'

>>> from yakutils import datetime_to_iso8601
>>> datetime_to_iso8601(dt.datetime.utcnow())
'2020-01-26T19:04:40.219668Z'

>>> from yakutils import datetime_to_unixtimestamp
>>> datetime_to_unixtimestamp(dt.datetime.utcnow())
1580065524

>>> from yakutils import iso8601_to_datetime
>>> iso8601_to_datetime('2020-01-26T19:04:40.219668Z')
datetime.datetime(2020, 1, 26, 19, 4, 40, 219668)

>>> from yakutils import md5
>>> md5('sully sullenberger')
'6ecd48fbe614fa7d1f87bcee3713f733'

>>> from yakutils import sha1
>>> sha1('sully sullenberger')
'593e310d210500c0a7a9f379e209063a4a78cbf4'

>>> from yakutils import iter_json
>>> for item in iter_json('/path/to/data.json'):
...   print(item)
[
  {
    'name': 'Tomatillo',
    'age': 27
  },
  # ...
]

>>> import json
>>> from yakutils import JSONEncoder
>>> json.dumps({'now': dt.datetime.utcnow}, JSONEncoder)

>>> from yakutils import setup_logging
>>> log = setup_logging(__name__)
>>> log.debug('Setting up widget ...')

>>> from yakutils import random_string
>>> random_string(20)
'k4a9ue7TDjOC3p3oN0dl'

>>> from yakutils import update_qs
>>> update_qs('https://nickficano.com.com/?q=asdf&pi=3.14', pi=6.28)
'https://nickficano.com.com/?q=asdf&pi=6.28'
```
