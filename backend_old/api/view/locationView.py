import collections

from django.http import JsonResponse
from rest_framework.views import APIView

from backend_old.api.cqrs_c.location import add, delete, update
from backend_old.api.cqrs_q.location import get_user_portfolio
from backend_old.api.view.common import get_auth_ok_response_template


#
def validate_actions(correct_actions, to_check_actions):
    return collections.Counter(correct_actions) == collections.Counter(
        to_check_actions)


class LocationView(APIView):
    def patch(self, request, portfolio, location_name):
        print("LocationsView patch")

        response = get_auth_ok_response_template(request)
        response["payload"]["status"] = update(request.username, portfolio,
                                               location_name, request.data)
        return JsonResponse(response)

    def delete(self, request, portfolio, name):
        response = get_auth_ok_response_template(request)
        r = delete(request.username, portfolio, name)
        response["payload"]["status"] = r
        return JsonResponse(response)

    def get(self, request, portfolio=None):
        print("location get")
        response = get_auth_ok_response_template(request)
        if portfolio:
            print(f"get all locations for {portfolio=}")
            username_locations = get_user_portfolio(request.username,
                                                    portfolio)
            r = {}
            j = 0
            for location in username_locations:
                r[j] = {"section": location.section,
                        "type": location.type,
                        # todo refactor to latitude & longitude
                        "lat": location.latitude,
                        "lon": location.longitude,
                        "name": location.name}
                j += 1

            payload = {"status": True, "content": r}
            result = payload

            response["payload"] = result
            return JsonResponse(response)
        return JsonResponse(response)

    # todo add type & section as param
    def post(self, request, portfolio, name):
        print("post locations", portfolio, name)
        response = get_auth_ok_response_template(request)
        if not request.synchronizer_token_match:
            print('add not valid')
            payload = {"status": False}
            print(request)
            result = payload
            response["payload"] = result
            return JsonResponse(response)

        status = add(request.username,
                     portfolio,
                     name,
                     request.data)

        r = status == "created"
        payload = {"status": r, "reason": status}
        result = payload

        response["payload"] = result
        return JsonResponse(response)
