Login request validator
=========================

Once the frontend sends a *login_request*, the request needs to
be validated against the following schema:

.. include:: ../../../../../schemas/internal_api/login_request.yaml
    :literal:

The interface for the validation is as follows:

.. autofunction:: src_django.api.validator.internal_api.login.validate_internal_login
