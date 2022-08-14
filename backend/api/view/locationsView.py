from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.comm.comm import decode_data
from backend.api.config.main import get_actions_for_routes, \
    INTERNAL_SERVER_ERROR_MESSAGE
from backend.api.cqrs_c.location import add, delete
from backend.api.cqrs_q.location import get_all, get_all_by_username
from backend.api.mode.type_validator import _check_request_data
from backend.api.view.comm import check_request_contains
from backend.api.view.comm import get_auth_ok_response_template


import collections

class LocationAction:

    def __init__(self):
        """"""

    def perform_action(self, request):
        raise Exception("action not implemented")


class AddSingle(LocationAction):

    def perform_action(self, request):

        if (not _check_request_data(request.data)
                or not request.synchronizer_token_match
                or not request.body):
            print('add not valid')
            payload = {"status": False}
            print(request)
            return payload

        body_content = decode_data(request.body)

        status = add(
            request.username,
            body_content["section"],
            body_content["type"],
            body_content["latitude"],
            body_content["longitude"])

        payload = {"status": status}
        return payload


class SelectUsername(LocationAction):

    def perform_action(self, request):
        print("select by username")
        # print("add single")
        # print("username", request.username)

        username_locations = get_all_by_username(request.username)
        payload = {"status": True, "content": username_locations}
        return payload


class SelectAll(LocationAction):

    def perform_action(self, request):
        print("select all")

        all_locations = get_all()
        payload = {"status": True, "content": all_locations}
        return payload


class DeleteSingle(LocationAction):
    """"""

    def perform_action(self, request):
        print("delete single")

        body_content = decode_data(request.body)

        return {
            "status": delete(body_content["index"])
        }



def validate_actions(correct_actions, to_check_actions):
    # print(f"{correct_actions=}")
    # print(f"{to_check_actions=}")
    return collections.Counter(correct_actions) == collections.Counter(
        to_check_actions)


def serialize(route, action):
    return route + ";" + action


class LocationsView(APIView):

    def __init__(self):

        self.route = "locations"

        self.actions = {
            serialize(self.route, "create single"): AddSingle(),
            serialize(self.route, "select all"): SelectAll(),
            serialize(self.route, "select username"): SelectUsername(),
            serialize(self.route, "delete single"): DeleteSingle()
        }

        if not validate_actions(
                correct_actions=get_actions_for_routes()[self.route],
                to_check_actions=list(self.actions)
        ):
            raise Exception(INTERNAL_SERVER_ERROR_MESSAGE)

        print(f"validated {self.route}")

    # def put(self, request):
    #     """update by editing existing"""
    #     print("put locations")

    # def post(self, request, pk=None):
    #     print("delete locations")
    #
    #     roles = request.roles
    #     response = {"auth": {"status": True,
    #                          "access-token": request.access_token,
    #                          "refresh-token": request.refresh_token}}
    #
    #     if not _has_permission(roles, ACTIONS.DELETE) or not pk:
    #         response["payload"] = {"status": False}
    #         return JsonResponse(response)
    #
    #     print("pk present", pk)
    #
    #     status = delete(pk)
    #
    #     if not status:
    #         response["payload"] = {"status": False}
    #         return JsonResponse(response)
    #
    #     response["payload"] = {"page": "put device"}
    #     return JsonResponse(response)

    def post(self, request):
        print()
        print("post locations")

        response = get_auth_ok_response_template(request)

        action = request.action

        if action in self.actions:
            result = self.actions[action].perform_action(request)

        else:
            result = self.unsupported_action()

        response["payload"] = result
        return JsonResponse(response)

    @staticmethod
    def unsupported_action():
        print('unsupported action')
        return {"status": False}

    # def action_get_all(self, request, roles):
    #     print("get locations")
    #     if not _has_permission(roles, ACTIONS.GET_ALL):
    #         payload = {"status": False}
    #     else:
    #         all_locations = get_all()
    #         payload = {"status": True, "content": all_locations}
    #     print("getting by username")
    #     username_locations = get_all_by_username(request.username)
    #     print("for usenrame", username_locations)
    #     return payload

    # def location_add(self, request, roles):
    #     payload = None
    #
    #     print("username", request.username)
    #
    #     if (not _has_permission(roles, ACTIONS.ADD)
    #             or not _check_request_data(request.data)
    #             or not request.synchronizer_token_match
    #             or not request.body):
    #         print('add not valid')
    #         payload = {"status": False}
    #
    #         print(request)
    #
    #         # response["payload"] = {"status": False}
    #     else:
    #         body_content = decode_data(request.body)
    #
    #         status = add(
    #             request.username,
    #             body_content["section"],
    #                      body_content["type"],
    #                      body_content["latitude"],
    #                      body_content["longitude"])
    #
    #         payload = {"status": status}
    #         # response["payload"] = {"status": status}
    #     return payload

    # def get(self, request):
    #     print("get locations")
    #
    #     response = {"auth": {"status": True,
    #                          "access-token": request.access_token,
    #                          "refresh-token": request.refresh_token}}
    #
    #     roles = request.roles
    #
    #     if not _has_permission(roles, ACTIONS.GET_ALL):
    #         response["payload"] = {"status": False}
    #         return JsonResponse(response)
    #
    #     print("access granted, getting roles")
    #     all_locations = get_all()
    #     [print(i) for i in all_locations]
    #     response["payload"] = {"status": True, "content": all_locations}
    #     return JsonResponse(response)
