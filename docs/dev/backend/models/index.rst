Models
==========

This module represents the data format of objects that are being read from
and written into a database. The only thing that the Flexopt application
saves is the flexibility offers calculated by the aggregators. Those
flexibility offers can be shown as a total flexibility for an aggregator and
as a individual flexibility per building. Accordingly, two types of data
can be found in the database: flexibility per aggregator and flexibility per
building. Both types of data have a given time interval in which they are
valid.


Content
-------

.. toctree::
    :maxdepth: 1

    aggregator_flexibility
    building_flexibility
    user_session

