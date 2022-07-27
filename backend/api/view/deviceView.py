import json

from django.http import JsonResponse
from rest_framework.views import APIView
from backend.api.comm.comm import decode_data
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from backend.api.cqrs_c.device import create
from backend.api.cqrs_q.device import get_all, get_by_id

#
#
# class DeviceView(ModelViewSet):
#
#     @action(methods=['post'], detail=True)
#     def set_password(self, request, pk=None):
#         print("llll")
#
#     @classmethod
#     def get_extra_actions(cls):
#         return []

class DeviceView(APIView):

    # def post(self, request, pk):
    def post(self, request):
        print("todo checking role")

        print("create new device")

        if request.body:
            body_content = decode_data(request.body)
            print(f"{body_content=}")

            create(
                # device_id=pk,
                device_type=body_content["device_type"][0],
                consumption=body_content["consumption"][0],
                data_id=body_content["data_id"][0]
            )

        response = {
            "auth": {
                "status": True,
                "access-token": request.access_token,
                "refresh-token": request.refresh_token
            },
            "payload": {
                "page": "put device",
                "device_type =": body_content["device_type"][0],
                "consumption = ":body_content["consumption"][0],
                "data_id = ":body_content["data_id"][0]

        }
        }

        return JsonResponse(response)

    def get(self, request, pk=None):
        print("todo checking role")

        if pk:
            print("pk present ------------------")
            print("pk,", pk)
        else:
            print("no pk -------------")


        if request.body:
            body_content = decode_data(request.body)
            print(f"{body_content=}")


            # create(
                # device_id=pk,
            #     device_type=body_content["device_type"][0],
            #     consumption=body_content["consumption"][0],
            #     data_id=body_content["data_id"][0]
            # )

        print("get")

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


    # def post(self, request):
    #     print("logout post")
    #
    #     print("try logout")
    #     logout(request.refresh_token)
    #     print("logout done")
    #
    #     response = {
    #         "auth": {
    #             "status": True,
    #             "access-token": None,
    #             "refresh-token": None
    #         },
    #         "payload": {
    #             "page": "logout",
    #         }
    #     }
    #
    #     return JsonResponse(response)
