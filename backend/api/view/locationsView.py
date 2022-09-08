import collections

from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.comm.comm import bytes_to_json
from backend.api.cqrs_c.location import add, delete
from backend.api.cqrs_q.location import get_user_portfolio
from backend.api.mode.type_validator import _check_request_data
from backend.api.view.comm import get_auth_ok_response_template


#
def validate_actions(correct_actions, to_check_actions):
    return collections.Counter(correct_actions) == collections.Counter(
        to_check_actions)


class LocationsView(APIView):

    def delete(self, request):
        print("delete single")

        body_content = bytes_to_json(request.body)

        return {
            "status": delete(body_content["index"])
        }

    def get(self, request, pn):

        if not pn:
            # all_locatio/ns = get_all()
            payload = {"status": False, "content": "all_locations"}
            result = payload
        else:
            # api.beyond.com/portfolios/p1/locations/
            print()
            # print("get locations by username")
            # todo check if get all or for this user

            response = get_auth_ok_response_template(request)

            username_locations = get_user_portfolio(request.username,
                                                    portfolio_name=pn)

            r = {}
            j = 0
            for i in username_locations:
                r[j] = {
                    # "pk": i.name,
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

    # todo add type & section
    def post(self, request):
        print()
        print("post locations")

        response = get_auth_ok_response_template(request)

        print(f"{_check_request_data(request.data)=}")
        print(f"{request.synchronizer_token_match=}")
        print(f"{request.body=}")

        if (
                not _check_request_data(request.data)
                or not request.synchronizer_token_match
                or not request.body
        ):
            print('add not valid')
            payload = {"status": False}
            print(request)
            result = payload

        else:
            body_content = bytes_to_json(request.body)

            status = add(
                body_content["portfolio"],
                body_content["section"],
                body_content["type"],
                body_content["latitude"],
                body_content["longitude"]
            )

            payload = {"status": status}
            result = payload

        response["payload"] = result
        return JsonResponse(response)
