Algorithm view
===============

Algorithm view listens for HTTP post on BASE_URL/algorithm.
There may or may not be a trailing slash following the above-mentioned URL.
Once an aggregator logs in, and gets the flexibility demands for a specific
date, the next step is to calculate the possible flexibility offer for selected
buildings and intervals within the selected date.
Once the request arrives, it is validated. Once validated, the request
is parsed and the information is forwarded towards the Flexopt algorithm.
Once the calculation is completed, it is forwarded to the frontend. If for
any reason during this workflow an error occurs, an appropriate error message
will be sent.

- If validation fails, the response will contain a message 'invalid request'

All the information needed to pass the validation needs to be JSON formatted
and be located in the request body. The validation is done using the following
schema:

.. include:: ../../../../schemas/internal_api/algorithm_request.yaml
    :literal:

As can be seen from the schema, the expected message type **must** be
*algorithm_request*. As stated, the response can either contain the
needed information or an error message. Although the generated responses are
not internally validated by JSON schemas, they can be described as follows:

.. include:: ../../../../schemas/backend_responses/algorithm_response.yaml
    :literal:

The response type will always be *algorithm_response*.
