Beyond Verifier
===============

This middleware verifies whether the incoming Beyond requests contain a
signature, and if signature exists, if it is valid.

It processes the following requests from Beyond:

- flexibility_offer_by_aggregator
- flexibility_offer_by_building

The schemas are as follows:

- flexibility_offer_by_aggregator

.. include:: ../../../../schemas/external_api/flexibility_offer_by_aggregator.yaml
    :literal:

- flexibility_offer_by_building

.. include:: ../../../../schemas/external_api/flexibility_offer_by_building.yaml
    :literal:

If the signature is invalid or nonexistent a false status message will be
sent as a response. It the signature is valid, the message is forwarder to the
view.

For more information about the signature procedure, refer to this document:
(beyond_verification_procedure.txt)

.. include:: ../../../api/beyond_verification_procedure.txt
    :literal:
