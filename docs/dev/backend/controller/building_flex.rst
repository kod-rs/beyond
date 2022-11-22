.. _controller-building_flex:

Building Flexibility Offer
============================

The module offers *add* and *get* functions for building flexibilities.

Aggregator can save a flexibility into a database. That flexibility consists
of a time period in which it is valid, building id and the flexibility amount.

Once saved, that flexibility can be retrieved by sending the desired interval
and the building id to the controller which then returns the desired
flexibility, if a flexibility satisfying the input data (interval and user id)
exists.

.. automodule:: src_django.api.controller.building_flex
   :members:
   :undoc-members:
   :show-inheritance:
