Buildings request validator
============================

The validator validates building related request from the frontend.
There are two requests of such nature:

- buildings_by_user_id_request
- building_info_request


buildings_by_user_id_request
-------------------------------
Once the frontend sends a *buildings_by_user_id_request*, the request needs to
be validated against the following schema:

.. include:: ../../../../../schemas/internal_api/buildings_by_user_id_request.yaml
    :literal:

The interface for the validation is as follows:

.. autofunction:: src_django.api.validator.internal_api.buildings.validate_buildings_by_usr_id_req


building_info_request
-----------------------
Once the frontend sends a *building_info_request*, the request needs to
be validated against the following schema:

.. include:: ../../../../../schemas/internal_api/building_info_request.yaml
    :literal:

The interface for the validation is as follows:

.. autofunction:: src_django.api.validator.internal_api.buildings.validate_building_info_req




