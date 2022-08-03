from django.db import models
from django.http import JsonResponse
from rest_framework.views import APIView


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


from backend.api.comm.comm import decode_data


class TestCrudView(APIView):

    def put(self, request):
        print("put")

        # if request.role = "a"

        print(request.body)

        body_content = decode_data(request.body)
        data_id = body_content["id"][0]
        new_value = body_content["newValue"][0]

        # body_content = json.loads(request.body.decode("utf-8"))
        # print("adding", body_content["id"], body_content["newValue"])

        add_or_update(
            data_id,
            new_value
            # body_content["id"], body_content["newValue"]
        )

        response = {
            "auth": {
                "status": True,
                "access-token": None,
                "refresh-token": None
            },
            "payload": {
                "page": "logout",
                "result": get_one(data_id).val_val
            }
        }

        return JsonResponse(response)

    def get(self):
        """read"""

        print("get test curd")

        r = get_all()

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
