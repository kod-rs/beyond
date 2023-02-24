Custom Session
==============

This middleware verifies whether the user session is valid or has not expired.

It processes the following requests from frontend:

- algorithm_request
- buildings_by_user_id_request
- building_info_request
- flexibility_demand_request
- flexibility_offer_confirmation_request

If the session token is invalid or has expired a false status message will be
prompted. If the access token is valid, middleware checks whether token has
expired. If token is valid, response is forwarded to the view.
