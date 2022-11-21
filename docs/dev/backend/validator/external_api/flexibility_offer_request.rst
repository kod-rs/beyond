Flexibility offer request validator
====================================

The validator validates flexibility offer related requests from the Beyond API.
There are two requests of such nature:

- flexibility_offer_by_aggregator
- flexibility_offer_by_building


flexibility_offer_by_aggregator
-------------------------------

If the Beyond platform needs to get flexibility offers for a specific
combination of a user and a time interval, it sends this request which is
validated against the following schema:

.. include:: ../../../../../schemas/external_api/flexibility_offer_by_aggregator.yaml
    :literal:

The interface for the validation is as follows:

.. autofunction:: src_django.api.validator.external_api.flexibility_offer_request.validate_flex_offer_req_agr


flexibility_offer_by_building
-------------------------------

If the Beyond platform needs to get flexibility offers for a specific
combination of a building and a time interval, it sends this request which is
validated against the following schema:

.. include:: ../../../../../schemas/external_api/flexibility_offer_by_building.yaml
    :literal:

The interface for the validation is as follows:

.. autofunction:: src_django.api.validator.external_api.flexibility_offer_request.validate_flex_offer_req_building



