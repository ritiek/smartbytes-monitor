smartbytes-monitor
==================

Python package to monitor your Airtel broadband network stats like remaining data, days
left, etc.

Installation
------------

::

    pip install smartbytes-monitor

or if you like to live on the bleeding edge:

::

    python setup.py install

Usage
-----

Just launch the command ``smartbytes`` and it will tell you about your
broadband plan information.

::

    $ smartbytes
    =============================
    Total data : 30.0 GB
    Data left  : 2.6 GB
    Days left  : 1 day(s)
    DSL number : 0172xxxxxxx:_dsl
    =============================
    
This tool can also used as a library:

::

    >>> import smartbytes
    >>> airtel = smartbytes.smartbytes()
    >>> airtel.data_total
    u'30.0 GB'
    >>> airtel.data_left
    u'2.6 GB'
    >>> airtel.days_left
    u'1 day(s)'
    >>> airtel.dsl_number
    u'0172xxxxxxx:_dsl'

License
-------

``The MIT License``
