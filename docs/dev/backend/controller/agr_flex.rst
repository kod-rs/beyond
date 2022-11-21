.. _controller-agr_flex:

Aggregator Flexibility Offer
============================

The module offers *add* and *get* functions for aggregator flexibilities.

Aggregator can save a flexibility into a database. That flexibility consists
of a time period in which it is valid, user id and the flexibility amount.

Once saved, that flexibility can be retrieved by sending the desired interval
and the user id to the controller which then returns the desired flexibility,
if a flexibility satisfying the input data (interval and user id) exists.

.. automodule:: src_django.api.controller.agr_flex
   :members:
   :undoc-members:
   :show-inheritance:
