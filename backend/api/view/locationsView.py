import json

from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.comm.comm import decode_data
from backend.api.cqrs_q.location import get_all
from backend.api.cqrs_c.location import add, delete
from backend.api.config.main import ROLES
from django.core import serializers


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

        action = request.action
        print(action)

        print("post locations")


        if action == "add":


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

                if request.body:
                    body_content = decode_data(request.body)
                    print(f"{body_content=}")

                    section = body_content["section"]
                    location_type = body_content["type"]
                    latitude = body_content["latitude"]
                    longitude = body_content["longitude"]

                    # d = add(**body_content)
                    d = add(section, location_type, latitude, longitude)

                    response["payload"] = {
                        "status": True
                    }

                    return JsonResponse(response)

            response["payload"] = {"status": False}
            return JsonResponse(response)

        elif action == "get all":
            print("get locations")

            response = {
                "auth": {
                    "status": True,
                    "access-token": request.access_token,
                    "refresh-token": request.refresh_token
                }
            }

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

        elif action == "delete":
            print("delete")

            response = {
                "auth": {
                    "status": True,
                    "access-token": request.access_token,
                    "refresh-token": request.refresh_token
                }
            }


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


                response["payload"] = {
                    "status": True,
                    "content": d
                }

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

            response["payload"] = {
                "status": True,
                "content": d
            }


        else:
            response["payload"] = {"status": False}

        print("response", response)

        return JsonResponse(response)
