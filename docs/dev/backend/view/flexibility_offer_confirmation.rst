Flexibility offer confirmation view
====================================

Algorithm view listens for HTTP post on
BASE_URL/flexibility_offer_confirmation.
There may or may not be a trailing slash following the above-mentioned URL.
Once an aggregator logs in, gets the flexibility demands for a specific
date, and calculates the possible flexibility offer for selected buildings and
date, the resulting flexibility may be saved. Once the save request, called
flexibility offer confirmation, arrives, it is validated. Once validated, the
request is parsed and the information is forwarded towards the database
controller which saves the data into a database. If for any reason during this
workflow an error occurs, an appropriate error message
will be sent.

- If validation fails, the response will contain a message 'invalid request'
- If the database save fails, the response will contain a message 'database save
  failed'

All the information needed to pass the validation needs to be JSON formatted
and be located in the request body. The validation is done using the following
schema:

.. include:: ../../../../schemas/internal_api/flexibility_offer_confirmation.yaml
    :literal:

As can be seen from the schema, the expected message type **must** be
*flexibility_offer_confirmation_request*. As stated, the response can either
contain the needed information or an error message. Although the generated
responses are not internally validated by JSON schemas, they can be described
as follows:

.. include:: ../../../../schemas/backend_responses/flexibility_offer_confirmation_response.yaml
    :literal:

The response type will always be *flexibility_offer_confirmation_response*.
