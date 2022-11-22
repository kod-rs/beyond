Flexibility offer confirmation validator
=========================================

Once the frontend sends a *flexibility_offer_confirmation*, the request needs to
be validated against the following schema:

.. include:: ../../../../../schemas/internal_api/flexibility_offer_confirmation.yaml
    :literal:

The interface for the validation is as follows:

.. autofunction:: src_django.api.validator.internal_api.flexibility_offer_confirmation.validate_flexibility_offer_confirmation
