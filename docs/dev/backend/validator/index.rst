Validator
==========

Validator module is used to validate incoming POST requests to the backend.
POST requests can come from the frontend (internal API) or from the
Beyond platform (external API). Validations are done using JSON schemas.
JSON schemas used for validation can be found in the corresponding docs for
a specific request.

Content
-------

.. toctree::
    :maxdepth: 1

    common
    external_api/index
    internal_api/index