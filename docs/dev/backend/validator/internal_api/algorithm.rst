Algorithm request validator
===========================

If the frontend needs to get flexibility amount for a specific
combination of buildings and a time interval, it sends *algorithm_request*
which is validated against the following schema:

.. include:: ../../../../../schemas/internal_api/algorithm_request.yaml
    :literal:

The interface for the validation is as follows:

.. automodule:: src_django.api.validator.internal_api.algorithm
   :members:
   :undoc-members:
   :show-inheritance:

