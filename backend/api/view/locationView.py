import collections

from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.comm.comm import bytes_to_json
from backend.api.cqrs_c.location import add, delete, update
from backend.api.cqrs_q.location import get_user_portfolio
from backend.api.mode.type_validator import _check_request_data
from backend.api.view.comm import get_auth_ok_response_template


#
def validate_actions(correct_actions, to_check_actions):
    return collections.Counter(correct_actions) == collections.Counter(
        to_check_actions)


class LocationsView(APIView):
    def patch(self, request, portfolio, section, _type):
        print("LocationsView patch")

        response = get_auth_ok_response_template(request)
        response["payload"]["status"] = update(request.username, portfolio, section, _type, request.data)
        return JsonResponse(response)

    # path("location/<str:portfolio>/<str:section>/<str:type>", LocationsView.as_view()),

    def delete(self, request, portfolio, section, _type):
        print("delete single", portfolio, section, _type)

        response = get_auth_ok_response_template(request)

        r = delete(request.username,portfolio, section, _type)

        response["payload"]["status"] = r
        return JsonResponse(response)

    def get(self, request, portfolio,section, _type):
        print(f"locations get {portfolio=} {section=} {_type=}")

        response = get_auth_ok_response_template(request)

        username_locations = get_user_portfolio(request.username,portfolio)

        r = {}
        j = 0
        for i in username_locations:
            r[j] = {
                "section": i.section,
                "type": i.type,
                # todo refactor to latitude & longitude
                "lat": i.latitude,
                "lon": i.longitude,
            }

            j += 1

        payload = {"status": True, "content": r}
        result = payload

        response["payload"] = result
        return JsonResponse(response)

    # todo add type & section as param
    def post(self, request):
        print("post locations")

        response = get_auth_ok_response_template(request)

        # print(f"{_check_request_data(request.data)=}")
        # print(f"{request.synchronizer_token_match=}")

        # todo
        if (
                # not _check_request_data(request.data) or
                not request.synchronizer_token_match
                # or not request.body
        ):
            print('add not valid')
            payload = {"status": False}
            print(request)
            result = payload

        else:

            status = add(
                request.username,
                request.data["portfolio"],
                request.data["section"],
                request.data["type"],
                request.data["latitude"],
                request.data["longitude"]
            )

            r = status == "created"

            payload = {"status": r, "reason": status}
            result = payload

        response["payload"] = result
        return JsonResponse(response)
