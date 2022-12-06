Flexibility demand view
========================

Flexibility demand view listens for HTTP post on BASE_URL/flexibility_demand.
There may or may not be a trailing slash following the above-mentioned URL.
Once an aggregator logs in, the aggregator will need to know what flexibility
demands for a specific date are currently offered by the Beyond platform.
Once the request arrives, it is validated. Once validated, the request
is parsed and the information is forwarded towards the Beyond platform.
Once the response is received, it is forwarded to the frontend. If for
any reason during this workflow an error occurs, an appropriate error message
will be sent.

- If validation fails, the response will contain a message 'invalid request'
- If the Beyond platform does not return the expected information, the response
  will be 'request failed'.

All the information needed to pass the validation needs to be JSON formatted
and be located in the request body. The validation is done using the following
schema:

.. include:: ../../../../schemas/internal_api/flexibility_demand_request.yaml
    :literal:


The message sent to Beyond is similar to the received flexibility demand
request. The difference being the fact that the message being sent to Beyond
has a signature field.  The request schema, although not validated on the
sender (FlexOpt) side is as follows:

.. include:: ../../../../schemas/backend_requests/flexibility_demand_request.yaml
    :literal:

For more information about the signature procedure, refer to this document:
(beyond_verification_procedure.txt)

.. include:: ../../../api/beyond_verification_procedure.txt
    :literal:

As can be seen from the schema, the expected message type **must** be
*flexibility_demand_request*. As stated, the response can either contain the
needed information or an error message. Although the generated responses are
not internally validated by JSON schemas, they can be described as follows:

.. include:: ../../../../schemas/backend_responses/flexibility_demand_response.yaml
    :literal:

The response type will always be *flexibility_demand_response*.


