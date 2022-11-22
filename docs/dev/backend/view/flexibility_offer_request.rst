Flexibility offer request view
=================================

Algorithm view listens for HTTP post on
BASE_URL/flexibility_offer_by_aggregator.
If an aggregator decides to save the flexibility offer to a database, that
means that the aggregator plans to offer said flexibility and it can then be
read by the Beyond platform. Once the request to read the flexibility offer
arrives from the Beyond platform, it is validated. Once validated, the
request is parsed and the information is forwarded towards the database
controller which saves the data into a database. If for any reason during this
workflow an error occurs, an appropriate error message
will be sent.

- If validation fails, the response will contain a message 'invalid request'
- If the database read fails, the response will contain a message
  'no data found'. More detailed response for read fail will not be given
  because such responses are considered bad practice from a cybersecurity point
  of view.

There are two types of requests that can be accessed through this view.

- flexibility_offer_by_aggregator
- flexibility_offer_by_building


flexibility_offer_by_aggregator
---------------------------------
The Beyond platform can request a flexibility offer that an aggregator can
provide on a given date. All the information needed to pass the validation
needs to be JSON formatted and be located in the request body. The validation
is done using the following schema:

.. include:: ../../../../schemas/external_api/flexibility_offer_by_aggregator.yaml
    :literal:

As can be seen from the schema, the expected message type **must** be
*flexibility_offer_by_aggregator*. As stated, the response can either
contain the needed information or an error message. Although the generated
responses are not internally validated by JSON schemas, they can be described
as follows:

.. include:: ../../../../schemas/backend_responses/flexibility_offer_by_aggregator_response.yaml
    :literal:

The response type will always be *flexibility_offer_by_aggregator_response*.

flexibility_offer_by_building
---------------------------------
The Beyond platform can request a flexibility offer that a building can
provide on a given date. All the information needed to pass the validation
needs to be JSON formatted and be located in the request body. The validation
is done using the following schema:

.. include:: ../../../../schemas/external_api/flexibility_offer_by_building.yaml
    :literal:

As can be seen from the schema, the expected message type **must** be
*flexibility_offer_by_building*. As stated, the response can either
contain the needed information or an error message. Although the generated
responses are not internally validated by JSON schemas, they can be described
as follows:

.. include:: ../../../../schemas/backend_responses/flexibility_offer_by_building_response.yaml
    :literal:

The response type will always be *flexibility_offer_by_building_response*.