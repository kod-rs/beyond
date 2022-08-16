import re

from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.comm.comm import decode_data
from backend.api.config.main import ROLES, ACTIONS
from backend.api.cqrs_c.location import add, delete
from backend.api.cqrs_q.location import get_all

permissions = {
    ROLES.AGGREGATOR_AND_MANAGER.value: [
        ACTIONS.ADD, ACTIONS.GET_ALL, ACTIONS.DELETE],
    ROLES.AGGREGATOR.value: [
        ACTIONS.ADD, ACTIONS.GET_ALL, ACTIONS.DELETE],
    ROLES.BUILDING_MANAGER.value: [
        ACTIONS.ADD, ACTIONS.GET_ALL]}


class LocationsView(APIView):

    def put(self, request):
        pass

    def patch(self, request):
        pass

    def delete(self, request, pk=None):
        roles = request.roles
        response = {"auth": {"status": True,
                             "access-token": request.access_token,
                             "refresh-token": request.refresh_token}}

        if not _has_permission(roles, ACTIONS.DELETE) or not pk:
            response["payload"] = {"status": False}
            return JsonResponse(response)

        status = delete(pk)

        if not status:
            response["payload"] = {"status": False}
            return JsonResponse(response)

        response["payload"] = {"page": "put device"}
        return JsonResponse(response)

    def post(self, request):
        response = {"auth": {"status": True,
                             "access-token": request.access_token,
                             "refresh-token": request.refresh_token}}
        roles = request.roles
        action = request.action

        if action == ACTIONS.ADD.value:
            if (not _has_permission(roles, ACTIONS.ADD)
                    or not _check_request_data(request.data)
                    or not request.synchronizer_token_match
                    or not request.body):
                response["payload"] = {"status": False}
                return JsonResponse(response)

            body_content = decode_data(request.body)

            status = add(body_content["section"],
                         body_content["type"],
                         body_content["latitude"],
                         body_content["longitude"])

            response["payload"] = {"status": status}
            return JsonResponse(response)

        if action == ACTIONS.GET_ALL.value:
            if not _has_permission(roles, ACTIONS.GET_ALL):
                response["payload"] = {"status": False}
                return JsonResponse(response)
            all_locations = get_all()
            response["payload"] = {"status": True, "content": all_locations}
            return JsonResponse(response)

        elif action == ACTIONS.DELETE.value:
            if not _has_permission(roles, ACTIONS.DELETE) or not request.body:
                response["payload"] = {"status": False}
                return JsonResponse(response)

            body_content = decode_data(request.body)
            index = body_content["index"]
            status = delete(index)
            response["payload"] = {"status": status}
            return JsonResponse(response)

        response["payload"] = {"status": False}
        return JsonResponse(response)

    def get(self, request):
        response = {"auth": {"status": True,
                             "access-token": request.access_token,
                             "refresh-token": request.refresh_token}}
        roles = request.roles

        if not _has_permission(roles, ACTIONS.GET_ALL):
            response["payload"] = {"status": False}
            return JsonResponse(response)

        all_locations = get_all()
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
