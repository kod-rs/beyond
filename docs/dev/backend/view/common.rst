View common module
==================

Common module contains functionalities used by more than one view module.
Therefore, those functionalities are contained within this *common* module.

Every time a view request processing fails for any reason, a false status
message is returned. Since it is a generic message that always has the same
structure with only the type and the error message being different, the false
status message is offered as a function contained in this module.

.. autofunction:: src_django.api.view.common.false_status


In order not to handle JSON decoding errors in each individual module, a
wrapper function is created that handles errors during decoding and returns
either an empty object (empty dictionary) or the decoded input message.

.. autofunction:: src_django.api.view.common.json_decode


Since the datetime object is sent via the JSON message as a RFC 3339 (iso
format) string, it needs to be decoded into a datetime.datetime object in
several views.

.. autofunction:: src_django.api.view.common.datetime_from_rfc_string


The process of connection to the Beyond platform is the same for all the view
modules that require such connection. The only difference is the methods that
the views need. This object offers all the methods needed by the modules that
communicate with the Beyond platform.

.. autoclass:: src_django.api.view.common.BeyondConnection
    :members:
    :undoc-members:
    :show-inheritance:


As stated in the BeyondConnection.req_building_by_usr_id the response will be
formatted as specified in the 'building_info_response.yaml' schema:

.. include:: ../../../../schemas/external_api/building_info_response.yaml
    :literal:

As stated in the BeyondConnection.req_building_info the response will be
formatted as specified in the 'buildings_by_user_id_response.yaml' schema:

.. include:: ../../../../schemas/external_api/buildings_by_user_id_response.yaml
    :literal:

As stated in the BeyondConnection.req_flex_demand the response will be
formatted as specified in the 'flexibility_demand_response.yaml' schema:

.. include:: ../../../../schemas/external_api/flexibility_demand_response.yaml
    :literal:

