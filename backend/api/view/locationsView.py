from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.config.main import LOCATION_ACTION
from backend.api.mode.type_validator import _check_request_data
from backend.api.view.comm import get_auth_ok_response_template
from backend.api.comm.comm import decode_data
from backend.api.cqrs_c.location import add, delete
from backend.api.cqrs_q.location import get_all, get_all_by_username
from backend.api.view.comm import check_request_contains
from backend.api.config.main import get_actions_for_routes, INTERNAL_SERVER_ERROR_MESSAGE
# from backend.api.c
# .
# permissions = {
#     ROLES.AGGREGATOR_AND_MANAGER.value: [
#         ACTIONS.ADD, ACTIONS.GET_ALL, ACTIONS.DELETE],
#     ROLES.AGGREGATOR.value: [
#         ACTIONS.ADD, ACTIONS.GET_ALL, ACTIONS.DELETE],
#     ROLES.BUILDING_MANAGER.value: [
#         ACTIONS.ADD, ACTIONS.GET_ALL]}


class LocationAction:

    def __init__(self):
        """"""

    def perform_action(self, request):
        raise Exception("action not implemented")


class AddSingle(LocationAction):
    """"""

    def perform_action(self, request):
        print("add single")
        print("username", request.username)

        # if (not _has_permission(roles, ACTIONS.ADD)
        if (not _check_request_data(request.data)
                or not request.synchronizer_token_match
                or not request.body):
            print('add not valid')
            payload = {"status": False}

            print(request)

        else:
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
        print(f"{body_content=}")
        index = body_content["index"]
        status = delete(index)
        payload = {"status": status}
        return payload

        # print("delete locations")

        # roles = request.roles
        # response = {"auth": {"status": True,
        #                      "access-token": request.access_token,
        #                      "refresh-token": request.refresh_token}}
        #
        # if not _has_permission(roles, ACTIONS.DELETE) or not pk:
        #     response["payload"] = {"status": False}
        #     return JsonResponse(response)
        #
        # print("pk present", pk)
        #
        # status = delete(pk)
        #
        # if not status:
        #     response["payload"] = {"status": False}
        #     return JsonResponse(response)
        #
        # response["payload"] = {"page": "put device"}
        # return JsonResponse(response)


# class ActionPerformer:
#
#     def __init__(self, action):
#         self.action = action
#
#     def execute_action(self, request):
#         return self.action.perform_action(request)

import collections
def validate_actions(correct_actions, to_check_actions):
    # print(f"{correct_actions=}")
    # print(f"{to_check_actions=}")
    return collections.Counter(correct_actions) == collections.Counter(to_check_actions)
    # return correct_actions == to_check_actions

class LocationsView(APIView):



    def __init__(self):

        self.route = "location"

        self.actions = {
            LOCATION_ACTION.ADD_SINGLE.value: AddSingle(),
            LOCATION_ACTION.SELECT_ALL.value: SelectAll(),
            LOCATION_ACTION.SELECT_BY_USERNAME.value: SelectUsername(),
            LOCATION_ACTION.DELETE_SINGLE.value: DeleteSingle()
        }

        r = get_actions_for_routes()[self.route]

        t = validate_actions(
            correct_actions=r,
            to_check_actions=list(self.actions)
        )
        if not t:
            raise Exception(INTERNAL_SERVER_ERROR_MESSAGE)

        # print("validating actions: ", t)
        # print("possible actions for location:", r)

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

        action = check_request_contains(request, "action", raise_exception=True)

        print(f"{action=}")

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

# def _has_permission(roles, action):
#     roles = set(roles).intersection(set(permissions.keys()))
#     for role in roles:
#         if action in permissions[role]:
#             return True
#     return False
