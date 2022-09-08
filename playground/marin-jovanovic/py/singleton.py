from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.comm.comm import bytes_to_json
from backend.api.config.main import get_actions_for_routes, \
    INTERNAL_SERVER_ERROR_MESSAGE
from backend.api.cqrs_c.location import add, delete
from backend.api.cqrs_q.location import  get_all_by_username,get_user_portfolio
from backend.api.mode.type_validator import _check_request_data
from backend.api.view.comm import get_auth_ok_response_template


import collections

class LocationAction:

    def __init__(self):
        """"""

    def perform_action(self, request):
        raise Exception("action not implemented")


class AddSingle(LocationAction):

    def perform_action(self, request):

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
            return payload

        body_content = bytes_to_json(request.body)

        status = add(
            body_content["portfolio"],
            body_content["section"],
            body_content["type"],
            body_content["latitude"],
            body_content["longitude"]
        )

        payload = {"status": status}
        return payload


class SelectUsername(LocationAction):

    def perform_action(self, request):
        print("select by username")

        # ip_obj = Location.objects.filter(portfolio__username=username)

        username_locations = get_all_by_username(request.username)
        payload = {"status": True, "content": username_locations}
        return payload
        # return {"status": False, "f": "todo"}

class SelectAll(LocationAction):

    def perform_action(self, request):
        print("select all")

        # all_locatio/ns = get_all()
        payload = {"status": False, "content": "all_locations"}
        return payload


class DeleteSingle(LocationAction):
    """"""

    def perform_action(self, request):
        print("delete single")

        body_content = bytes_to_json(request.body)

        return {
            "status": delete(body_content["index"])
        }



def validate_actions(correct_actions, to_check_actions):

    return collections.Counter(correct_actions) == collections.Counter(
        to_check_actions)


def serialize(route, action):
    return route + ";" + action


class LocationsView(APIView):

    def __init__(self):

        self.route = "locations"

        self.actions = {
            serialize(self.route, "create single"): AddSingle(),
            serialize(self.route, "select_all"): SelectAll(),
            serialize(self.route, "select username"): SelectUsername(),
            serialize(self.route, "delete single"): DeleteSingle()
        }

        if not validate_actions(
                correct_actions=get_actions_for_routes()[self.route],
                to_check_actions=list(self.actions)
        ):
            raise Exception(INTERNAL_SERVER_ERROR_MESSAGE)

        print(f"validated {self.route}")


    def get(self, request, pn):
        # api.beyond.com/portfolios/p1/locations/
        print()
        print("get locations by username")
        # todo check if get all or for this user

        response = get_auth_ok_response_template(request)


        username_locations = get_user_portfolio(request.username, portfolio_name=pn)


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

            j+=1


        payload = {"status": True, "content": r}
        result = payload



        print(f"{result=}")

        response["payload"] = result
        return JsonResponse(response)


    # todo add type & section
    def post(self, request):
        print()
        print("post locations")

        response = get_auth_ok_response_template(request)

        result = self.actions["locations;create single"].perform_action(request)

        # action = request.action
        #
        # print("check action")
        # print(f"{action=}")
        # print(f"{self.actions=}")

        # if action in self.actions:
        #     result = self.actions[action].perform_action(request)
        #
        # else:
        #     result = self.unsupported_action()

        response["payload"] = result
        return JsonResponse(response)

    @staticmethod
    def unsupported_action():
        print('unsupported action')
        return {"status": False}
