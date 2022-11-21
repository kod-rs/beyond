Buildings response validator
============================

The validator validates building related responses from the Beyond API.
There are two responses of such nature:

- buildings_by_user_id_response
- building_info_response


buildings_by_user_id_response
-------------------------------
Once the Beyond platform sends an answer to *buildings_by_user_id_request*,
*buildings_by_user_id_response*, that response needs to have the following
structure defined by this JSON schema:

.. include:: ../../../../../schemas/external_api/buildings_by_user_id_response.yaml
    :literal:

The interface for the validation is as follows:

.. autofunction:: src_django.api.validator.external_api.buildings.validate_buildings_by_usr_id_resp


building_info_response
-----------------------
Once the Beyond platform sends an answer to *building_info_request*,
*building_info_response*, that response needs to have the following
structure defined by this JSON schema:

.. include:: ../../../../../schemas/external_api/building_info_response.yaml
    :literal:

The interface for the validation is as follows:

.. autofunction:: src_django.api.validator.external_api.buildings.validate_building_info




