Login view
==========

Login view listens for HTTP post on BASE_URL/login. There may or may not be
a trailing slash following the above-mentioned URL.
Once the login request arrives, it is validated. Once validated, the request
is parsed and the login information is forwarded towards the Keycloak server.
Once the Keycloak response is received, it is forwarded to the frontend. If for
any reason during this workflow an error occurs, an appropriate error message
will be sent.

- If validation fails, the response will contain a message 'invalid request'
- If Keycloak does not return the expected information, the response will
  contain one of the following:

    - HTTP response error code (for example 404)
    - 'server connection error'
    - 'account not fully set up'
    - 'keycloak error', as a generic response to unexpected errors

All the information needed to pass the validation needs to be JSON formatted
and be located in the request body. The validation is done using the following
schema:

.. include:: ../../../../schemas/internal_api/login_request.yaml
    :literal:

As can be seen from the schema, the expected message type **must** be
*login_request*. As stated, the response can either contain the needed login
information or an error message. Although the generated responses are not
internally validated by JSON schemas, they can be described as follows:

.. include:: ../../../../schemas/backend_responses/login_response.yaml
    :literal:

The response type will always be *login_response*.


