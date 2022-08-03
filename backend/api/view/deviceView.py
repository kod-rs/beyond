from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.comm.comm import decode_data
from backend.api.cqrs_c.device import create
from backend.api.cqrs_q.device import get_all, get_by_id


class DeviceView(APIView):
    # create rename update delete

    # create
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
                "consumption = ": body_content["consumption"][0],
                "data_id = ": body_content["data_id"][0]

            }
        }

        return JsonResponse(response)

    def get(self, request, pk=None):
        print("todo checking role")

        if pk:
            print("pk present ------------------")
            print("pk,", pk)

            b = get_by_id(pk)
            print(b)

        else:
            print("no pk -------------")
            b = get_all()
            [print(i) for i in b]

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
