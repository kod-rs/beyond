Flexibility demand request validator
=======================================

Once the frontend sends a *flexibility_demand_request*, the request needs to
be validated against the following schema:

.. include:: ../../../../../schemas/internal_api/flexibility_demand_request.yaml
    :literal:

The interface for the validation is as follows:

.. autofunction:: src_django.api.validator.internal_api.flexibility_demand_request.validate_flexibility_demand_request
