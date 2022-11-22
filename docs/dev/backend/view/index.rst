View
==========

Views are endpoints that can be accessed by the Beyond platform or by the
frontend. URLs which can be accessed are as follows (with or without the
trailing slash):

- BASE_URL/login
- BASE_URL/buildings
- BASE_URL/flexibility_demand
- BASE_URL/algorithm
- BASE_URL/flexibility_offer_confirmation
- BASE_URL/flexibility_offer

BASE_URL is URL on which the Flexopt application will be running at.

Views are set up to receive and send messages as defined in the following two
documents.

First document being API and views for the external API where the
external API is an API between the Beyond platform and the backend.
External API:

.. include:: ../../../api/beyond_external_api.txt
    :literal:

Second document being API and views for the internal API where the
internal API is an API between the frontend and the backend.
Internal API:

.. include:: ../../../api/internal_api.txt
    :literal:

Content
-------

.. toctree::
    :maxdepth: 1

    common
    login
    building
    flexibility_demand
    algorithm
    flexibility_offer_confirmation
    flexibility_offer_request