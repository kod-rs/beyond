import json

from django.db import models

from rest_framework.views import APIView
from django.http import JsonResponse

class TestCRUD(models.Model):
    # primary
    id_val = models.CharField(max_length=200)
    val_val = models.CharField(max_length=200)


# c u
def add_or_update(a, b):
    """
    add or update key

    """
    k, _ = TestCRUD.objects.update_or_create(
        id_val=a, defaults={"val_val": b}
    )
    k.save()


# r
def rename(a, b):
    """
    add or update key

    """
    t = TestCRUD.objects.get(id_val=a)
    t.id_val = b
    t.save()


# d
def delete(key_type):
    instance = TestCRUD.objects.get(val_val=key_type)
    instance.delete()


def get_all():
    return [i for i in TestCRUD.objects.all().iterator()]


def get_one(id_val):
    return TestCRUD.objects.get(id_val=id_val)




class TestCrudView(APIView):

    def put(self, request):
        print("put")

        # if request.role = "a"

        body_content = json.loads(request.body.decode("utf-8"))
        # print(body_content["id"], body_content["newValue"])

        try:

            add_or_update(
                body_content["id"], body_content["newValue"]
            )

        except SQLwrongtype:
            "payload": {
                "success": False
            }

            "payload": {
                "success": False
            }


        response = {
            "auth": {
                "status": True,
                "access-token": None,
                "refresh-token": None
            },
            "payload": {
                "page": "logout",
                "result": get_one(body_content["id"]).val_val
            }
        }

        return JsonResponse(response)

    def get(self):
        """read"""

        response = {
            "auth": {
                "status": True,
                "access-token": None,
                "refresh-token": None
            },
            "payload": {
                "page": "logout",
            }
        }

        return JsonResponse(response)
