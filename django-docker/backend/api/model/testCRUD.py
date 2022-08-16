from django.db import models
from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.comm.comm import decode_data


class TestCRUD(models.Model):
    id_val = models.CharField(max_length=200)
    val_val = models.CharField(max_length=200)


def add_or_update(a, b):
    k, _ = TestCRUD.objects.update_or_create(id_val=a, defaults={"val_val": b})
    k.save()


def rename(a, b):
    t = TestCRUD.objects.get(id_val=a)
    t.id_val = b
    t.save()


def delete(key_type):
    instance = TestCRUD.objects.get(val_val=key_type)
    instance.delete()


def get_all():
    return [i for i in TestCRUD.objects.all().iterator()]


def get_one(id_val):
    return TestCRUD.objects.get(id_val=id_val)


class TestCrudView(APIView):

    def put(self, request):
        body_content = decode_data(request.body)
        data_id = body_content["id"][0]
        new_value = body_content["newValue"][0]
        add_or_update(data_id, new_value)

        response = {"auth": {"status": True,
                             "access-token": None,
                             "refresh-token": None},
                    "payload": {"page": "logout",
                                "result": get_one(data_id).val_val}}
        return JsonResponse(response)

    def get(self):
        _ = get_all()

        response = {"auth": {"status": True,
                             "access-token": None,
                             "refresh-token": None},
                    "payload": {
                        "page": "logout"}}
        return JsonResponse(response)
