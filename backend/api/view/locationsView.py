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

    # def patch(self, request):
    #     """update by replacing"""

    def delete(self, request, pk=None):
        print("todo checking role")

        roles = request.roles
        response = {
            "auth": {
                "status": True,
                "access-token": request.access_token,
                "refresh-token": request.refresh_token
            }
        }
        response["payload"] = {"status": False}

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

        roles = request.roles

        # todo check role
        if any(i in ROLES for i in roles):
            print("access granted")

            if request.body:
                body_content = decode_data(request.body)
                print(f"{body_content=}")


                d = add(**body_content)

                response["payload"] = {
                    "status": True
                }

                return JsonResponse(response)

        response["payload"] = {"status": False}
        return JsonResponse(response)


    def get(self, request):

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


        return JsonResponse(response)
