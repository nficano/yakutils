.. yakutils documentation master file, created by
   sphinx-quickstart on Tue Jan 28 08:11:12 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. container::

  .. image:: https://assets.nickficano.com/gh-yakutils.min.svg
    :width: 348px
    :height: 174px
    :align: center

########
yakutils
########

.. image:: https://img.shields.io/pypi/v/yakutils.svg
  :alt: Pypi
  :target: https://pypi.python.org/pypi/yakutils/

.. image:: https://img.shields.io/pypi/pyversions/yakutils.svg
  :alt: Python Versions
  :target: https://pypi.python.org/pypi/yakutils/

Yet another toolbox of Python 3 helper functions.
*************************************************

This package is available on PyPi, but its primary purpose is to allow one (me) to copy these into projects or to prevent one (me as well) from needing to Google how to write them (I'm looking at you csv.DictReader and csv.DictWriter).

This project is a continuous work-in-progress for me, and while its contents are specific to stuff that I use, pull requests are certainly welcome or hell, just fork it and use it as your collection of snippets.

Features
========
- No third-party dependencies.
- Can be installed or be used as a source to copy and paste snippets.

Installation
============

.. note:: I take security seriously, and as such, I highly recommend reviewing the source of ``_hashlib.py`` if you plan on using the hashing functions. I mean, I know I'm ethical not to do anything evil, but that doesn't mean you shouldn't verify it.

Method 1: Install with pip
--------------------------

To install yakutils with pip, run the following command in your terminal::

    $ pip install yakutils

Method 2: Install with pipenv
-----------------------------

To install yakutils with pipenv, run the following command in your terminal::

    $ pipenv install yakutils

Method 3: Install from source
-----------------------------

yakutils is actively developed on GitHub, where the source is `available <https://github.com/nficano/yakutils>`_.

You can either clone the public repository::

    $ git clone git://github.com/nficano/yakutils.git

Or, download the `tarball <https://github.com/nficano/yakutils/tarball/master>`_::

    $ curl -OL https://github.com/nficano/yakutils/tarball/master
    # optionally, zipball is also available (for Windows users).

Once you have a copy of the source, you can embed it in your Python package, or install it into your site-packages by running::

    $ cd yakutils
    $ pip install .

-------------------

Functions
=========

read_csv
--------

Read a csv file as a ``dict``.

.. code-block:: python

    >>> from yakutils import read_csv
    >>> read_csv('/path/to/data.csv')
    [
      {
        'id': 1,
        'name': 'Willie Wasabi',
        'username': 'horseradison',
      },
      # ...
    ]

read_json
---------

Read a json file as a ``dict`` or ``list`` (depending of course on the json document).

.. code-block:: python

    >>> from yakutils import read_json
    >>> read_json('/path/to/data.json')
    [
      {
        'id': 1,
        'name': 'Madeline Mountain-Dew',
        'username': 'codered1',
      },
      # ...
    ]

json_defaults
-------------

.. code-block:: python

  >>> import json
  >>> from decimal import Decimal
  >>> from yakutils import json_defaults
  >>> json.dumps({
  ...   'now': dt.datetime.utcnow(),
  ...   'today': dt.date.today(),
  ...   'time': dt.time(1,2,3),
  ...   'num': Decimal(2.777),
  ...}, default=json_defaults)
  '{"now": "2020-01-28T01:10:37.599281Z", "today": "2020-01-27", "time": "01:02:03", "num": 2.777}'


date_to_iso8601
---------------

.. code-block:: python

  >>> import datetime as dt
  >>> from yakutils import date_to_iso8601
  >>> date_to_iso8601(dt.date.today())
  '2020-01-26T00:00:00Z'

datetime_to_iso8601
-------------------

.. code-block:: python

  >>> from yakutils import datetime_to_iso8601
  >>> datetime_to_iso8601(dt.datetime.utcnow())
  '2020-01-26T19:04:40.219668Z'

datetime_to_unixtimestamp
-------------------------

.. code-block:: python

  >>> from yakutils import datetime_to_unixtimestamp
  >>> datetime_to_unixtimestamp(dt.datetime.utcnow())
  1580065524

iso8601_to_datetime
-------------------

.. code-block:: python

  >>> from yakutils import iso8601_to_datetime
  >>> iso8601_to_datetime('2020-01-26T19:04:40.219668Z')
  datetime.datetime(2020, 1, 26, 19, 4, 40, 219668)

md5
---

.. code-block:: python

  >>> from yakutils import md5
  >>> md5('sully sullenberger')
  '6ecd48fbe614fa7d1f87bcee3713f733'

sha1
----

.. code-block:: python

  >>> from yakutils import sha1
  >>> sha1('sully sullenberger')
  '593e310d210500c0a7a9f379e209063a4a78cbf4'

sha384
------

.. code-block:: python

  >>> from yakutils import sha384
  >>> sha384('sully sullenberger')
  '5986d690ec9df6daa53857b6d79d51abf8c18e9b43c0c5a7f9698f364245d31dc6d2558e01e225cc0d120cfda52646f8'


sha3_384
--------

.. code-block:: python

  >>> from yakutils import sha3_384
  >>> sha3_384('sully sullenberger')
  '9e3eb4f4507c52685ab62cd452e90c0c861d45cd621cc2f6cfd11485837935dc807f40fbfce32c61c9102b0b3cb6de8c'


setup_logging
-------------

.. code-block:: python

  >>> from yakutils import setup_logging
  >>> log = setup_logging(__name__)
  >>> log.debug('Setting up widget ...')


random_string
-------------

.. code-block:: python

  >>> from yakutils import random_string
  >>> random_string(20)
  'k4a9ue7TDjOC3p3oN0dl'

random_tolerance
----------------

.. code-block:: python

  >>> time.sleep(random_tolerance(1.0, 0.01))
  >>> a = random_tolerance(4.0, 0.25)
  >>> assert 3.0 <= a <= 5.0
  True

update_qs
---------

.. code-block:: python

  >>> from yakutils import update_qs
  >>> update_qs('https://nickficano.com.com/?q=asdf&pi=3.14', pi=6.28)
  'https://nickficano.com.com/?q=asdf&pi=6.28'
