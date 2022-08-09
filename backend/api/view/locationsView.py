import enum
import re

from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.comm.comm import decode_data
from backend.api.config.main import ROLES
from backend.api.cqrs_c.location import add, delete
from backend.api.cqrs_q.location import get_all


class ACTIONS(enum.Enum):
    ADD = 'add'
    GET_ALL = 'get all'
    DELETE = 'delete'


class LocationsView(APIView):
    # create rename update delete

    def put(self, request):
        """update by editing existing"""
        print("put locations")

    # def patch(self, request):
    #     """update by replacing"""

    def delete(self, request, pk=None):
        print("todo checking role")
        print("delete locations")

        roles = request.roles
        response = {"auth": {
            "status": True,
            "access-token": request.access_token,
            "refresh-token": request.refresh_token
        }, "payload": {"status": False}}

        # todo check role
        if not any(i in ROLES for i in roles):
            print("access not granted")
            return JsonResponse(response)

        if not pk:
            print("no pk -------------")
            return JsonResponse(response)

        print("pk present", pk)

        r = delete(pk)

        if request.body:
            body_content = decode_data(request.body)
            print(f"{body_content=}")

        response = {
            "auth": {
                "status": True,
                "access-token": request.access_token,
                "refresh-token": request.refresh_token
            },
            "payload": {
                "page": "put device",
            }
        }

        return JsonResponse(response)

    def post(self, request):
        """create"""

        response = {
            "auth": {
                "status": True,
                "access-token": request.access_token,
                "refresh-token": request.refresh_token
            }
        }

        if not _check_request_data(request.data):
            print('invalid data')
            response["payload"] = {"status": False}
            return JsonResponse(response)

        action = request.action
        print(action)

        print("post locations")

        if action == ACTIONS.ADD.value:
            roles = request.roles

            if request.synchronizer_token_match:
                print("sync token ok")
            else:

                response["payload"] = {"status": False}
                return JsonResponse(response)

            print(request.synchronizer_token_match)

            # todo check role
            if any(i in ROLES for i in roles):
                print("access granted")

                if request.body:
                    body_content = decode_data(request.body)
                    print(f"{body_content=}")

                    section = body_content["section"]
                    location_type = body_content["type"]
                    latitude = body_content["latitude"]
                    longitude = body_content["longitude"]

                    # d = add(**body_content)
                    d = add(section, location_type, latitude, longitude)

                    response["payload"] = {"status": True}

                    return JsonResponse(response)

            response["payload"] = {"status": False}
            return JsonResponse(response)

        elif action == ACTIONS.GET_ALL.value:
            print("get locations")

            roles = request.roles
            print(f"{roles=}")
            # todo check role
            if any(i in ROLES for i in roles):
                print("access granted")

                print("getting roles")

                d = get_all()

                [print(i) for i in d]

                response["payload"] = {
                    "status": True,
                    "content": d
                }

                print("returning location, everything ok")

            else:
                print("role check error")
                response["payload"] = {"status": False}

            # print("response", response)

            return JsonResponse(response)

        elif action == ACTIONS.DELETE.value:
            print("delete")

            roles = request.roles
            print(f"{roles=}")
            # todo check role
            if any(i in ROLES for i in roles):
                print("access granted")

                print("getting roles")

                if request.body:
                    body_content = decode_data(request.body)
                    print(f"{body_content=}")

                    index = body_content["index"]

                    d = delete(index)

                response["payload"] = {"status": True,
                                       "content": d}

            print("returning location, everything ok")
            return JsonResponse(response)

    def get(self, request):
        print("get locations")

        response = {
            "auth": {
                "status": True,
                "access-token": request.access_token,
                "refresh-token": request.refresh_token
            }
        }

        roles = request.roles

        # todo check role
        if any(i in ROLES for i in roles):
            print("access granted")

            print("getting roles")

            d = get_all()

            # print(d)
            [print(i) for i in d]
            # serialized_d = serializers.serialize('json', [d, ])

            response["payload"] = {"status": True,
                                   "content": d}

        else:
            response["payload"] = {"status": False}

        print("response", response)

        return JsonResponse(response)


def _check_request_data(request_data):
    if request_data['action'] not in [a.value for a in ACTIONS]:
        print('invalid action')
        return False

    if request_data['action'] != ACTIONS.ADD.value:
        return True

    if not _type_check(request_data['latitude'], float):
        return False

    if not _type_check(request_data['longitude'], float):
        return False

    if not _type_check(request_data['section'], str):
        return False

    if not _type_check(request_data['type'], str):
        return False

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
