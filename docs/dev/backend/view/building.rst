Building view
===============

Building view listens for HTTP post on BASE_URL/buildings. There may or may not
be a trailing slash following the above-mentioned URL.
Once the request arrives, it is validated. Once validated, the request
is parsed and the information is forwarded towards the Beyond platform.
Once the Beyond platform response is received, it is forwarded to the frontend.
If for any reason during this workflow an error occurs, an appropriate error
message will be sent.

- If validation fails, the response will contain a message 'invalid request'
- If the Beyond platform does not return the expected information, the response
  will be 'request failed'.

There are two types of requests that can be accessed through this view.

- buildings_by_user_id_request
- building_info_request

buildings_by_user_id_request
-----------------------------
When a user sends his user ID with this request type, a response, if
successful, will contain all the buildings associated with the user. Each of
those buildings shall have the following information:

- Building name
- Building address
- Building ID
- Building coordinates (longitude and latitude)

All the information needed to pass the validation needs to be JSON formatted
and be located in the request body. The validation is done using the following
schema:

.. include:: ../../../../schemas/internal_api/buildings_by_user_id_request.yaml
    :literal:

The message sent to Beyond is similar to the received request message.
The difference being the fact that the message being sent to Beyond
has a signature field.  The request schema, although not validated on the
sender (FlexOpt) side is as follows:

.. include:: ../../../../schemas/backend_requests/buildings_by_user_id_request.yaml
    :literal:

As can be seen from the schema, the expected message type **must** be
*buildings_by_user_id_request*. As stated, the response can either contain the
needed building information or an error message. Although the generated
responses are not internally validated by JSON schemas, they can be described
as follows:

.. include:: ../../../../schemas/backend_responses/buildings_by_user_id_response.yaml
    :literal:

The response type will always be *buildings_by_user_id_response*.


building_info_request
-----------------------------
When a user sends his user ID with this request type, a response, if
successful, will contain all the buildings associated with the user. Each of
those buildings shall have all the available timeseries information for that
building. Timeseries information contains an array *time, value* pairs.

All the information needed to pass the validation needs to be JSON formatted
and be located in the request body. The validation is done using the following
schema:

.. include:: ../../../../schemas/internal_api/building_info_request.yaml
    :literal:

As can be seen from the schema, the expected message type **must** be
*building_info_request*. As stated, the response can either contain the
needed building information or an error message. Although the generated
responses are not internally validated by JSON schemas, they can be described
as follows:

.. include:: ../../../../schemas/backend_responses/building_info_response.yaml
    :literal:

The response type will always be *building_info_response*.


 For more information about the signature procedure, refer to this document:
 (beyond_verification_procedure.txt)

.. include:: ../../../api/beyond_verification_procedure.txt
    :literal: