import enum
import re

from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.comm.comm import decode_data
from backend.api.config.main import ROLES, ACTIONS
from backend.api.cqrs_c.location import add, delete
from backend.api.cqrs_q.location import get_all, get_all_by_username


permissions = {
    ROLES.AGGREGATOR_AND_MANAGER.value: [
        ACTIONS.ADD, ACTIONS.GET_ALL, ACTIONS.DELETE],
    ROLES.AGGREGATOR.value: [
        ACTIONS.ADD, ACTIONS.GET_ALL, ACTIONS.DELETE],
    ROLES.BUILDING_MANAGER.value: [
        ACTIONS.ADD, ACTIONS.GET_ALL]}


class LocationAction:

    def __init__(self):
        """"""

    def perform_action(self, request):
        raise Exception("action not implemented")


class AddSingle(LocationAction):
    """"""

    def perform_action(self, request):
        print("add single")
        # print("username", request.username)
        #
        # # if (not _has_permission(roles, ACTIONS.ADD)
        # if (not _check_request_data(request.data)
        #         or not request.synchronizer_token_match
        #         or not request.body):
        #     print('add not valid')
        #     payload = {"status": False}
        #
        #     print(request)
        #
        # else:
        #     body_content = decode_data(request.body)
        #
        #     status = add(
        #         request.username,
        #         body_content["section"],
        #         body_content["type"],
        #         body_content["latitude"],
        #         body_content["longitude"])
        #
        #     payload = {"status": status}
        # return payload


class SelectUsername(LocationAction):

    def perform_action(self, request):
        print("select username")


class SelectAll(LocationAction):
    """"""

    def perform_action(self, request):
        print("select all")


class DeleteSingle(LocationAction):
    """"""

    def perform_action(self, request):
        print("delete single")

class Context:

    def __init__(self, action):
        self.action = action

    def set_action(self, action):
        self.action = action

    def execute_action(self):
        self.action.perform_action()



class LocationsView(APIView):
    # create rename update delete

    def put(self, request):
        """update by editing existing"""
        print("put locations")

    # def patch(self, request):
    #     """update by replacing"""

    def delete(self, request, pk=None):
        print("delete locations")

        roles = request.roles
        response = {"auth": {"status": True,
                             "access-token": request.access_token,
                             "refresh-token": request.refresh_token}}

        if not _has_permission(roles, ACTIONS.DELETE) or not pk:
            response["payload"] = {"status": False}
            return JsonResponse(response)

        print("pk present", pk)

        status = delete(pk)

        if not status:
            response["payload"] = {"status": False}
            return JsonResponse(response)

        response["payload"] = {"page": "put device"}
        return JsonResponse(response)

    def post(self, request):
        """create"""
        print("post locations")

        response = {"auth": {"status": True,
                             "access-token": request.access_token,
                             "refresh-token": request.refresh_token}}
        roles = request.roles
        action = request.action

        print(action)

        print()

        if action == ACTIONS.ADD.value:
            payload = self.location_add(request, roles)

        elif action == ACTIONS.GET_ALL.value:
            payload = self.action_get_all(request, roles)

        elif action == ACTIONS.DELETE.value:
            payload = self.delete_action_single(request, roles)

        else:
            payload = self.unssuported_action()

        response["payload"] = payload
        return JsonResponse(response)

    def unssuported_action(self):
        print('unsupported action')
        payload = {"status": False}
        return payload

    def delete_action_single(self, request, roles):
        if not _has_permission(roles, ACTIONS.DELETE) or not request.body:
            payload = {"status": False}
        else:

            body_content = decode_data(request.body)
            print(f"{body_content=}")
            index = body_content["index"]
            status = delete(index)
            payload = {"status": status}
        return payload

    def action_get_all(self, request, roles):
        print("get locations")
        if not _has_permission(roles, ACTIONS.GET_ALL):
            payload = {"status": False}
        else:
            all_locations = get_all()
            payload = {"status": True, "content": all_locations}
        print("getting by username")
        username_locations = get_all_by_username(request.username)
        print("for usenrame", username_locations)
        return payload

    def location_add(self, request, roles):
        payload = None

        print("username", request.username)

        if (not _has_permission(roles, ACTIONS.ADD)
                or not _check_request_data(request.data)
                or not request.synchronizer_token_match
                or not request.body):
            print('add not valid')
            payload = {"status": False}

            print(request)

            # response["payload"] = {"status": False}
        else:
            body_content = decode_data(request.body)

            status = add(
                request.username,
                body_content["section"],
                         body_content["type"],
                         body_content["latitude"],
                         body_content["longitude"])

            payload = {"status": status}
            # response["payload"] = {"status": status}
        return payload

    def get(self, request):
        print("get locations")

        response = {"auth": {"status": True,
                             "access-token": request.access_token,
                             "refresh-token": request.refresh_token}}

        roles = request.roles

        if not _has_permission(roles, ACTIONS.GET_ALL):
            response["payload"] = {"status": False}
            return JsonResponse(response)

        print("access granted, getting roles")
        all_locations = get_all()
        [print(i) for i in all_locations]
        response["payload"] = {"status": True, "content": all_locations}
        return JsonResponse(response)


def _check_request_data(request_data):
    if not _string_check(request_data['section']):
        return False

    if not _string_check(request_data['type']):
        return False

    return True


def _type_check(value, expected_type):
    try:
        expected_type(value)
        return True
    except ValueError:
        print(f'value={value} is not the expected type')
        return False


def _string_check(input_string):
    pattern = re.compile('^[čćžšđČĆŽŠĐA-Za-z0-9.,\\s]+$')

    if re.search(pattern, input_string):
        return True
    else:
        return False


def _has_permission(roles, action):
    roles = set(roles).intersection(set(permissions.keys()))
    for role in roles:
        if action in permissions[role]:
            return True
    return False
