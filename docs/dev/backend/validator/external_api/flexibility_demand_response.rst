Flexibility demand response validator
=======================================

Once the Beyond platform sends an answer to *flexibility_demand_request*,
*flexibility_demand_response*, that response needs to have the following
structure defined by this JSON schema:

.. include:: ../../../../../schemas/external_api/flexibility_demand_response.yaml
    :literal:

The interface for the validation is as follows:

.. autofunction:: src_django.api.validator.external_api.flexibility_demand_response.validate_flexibility_demand_response
