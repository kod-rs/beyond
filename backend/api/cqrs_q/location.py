import ast
import json

from django.core import serializers

from backend.api.model.location import Location


def get_all():
    t = serializers.serialize('json', Location.objects.all())
    t = json.loads(t)
    print(t)

    n = []
    for i in t:
        f = {}
        p = i["pk"]
        f["pk"] = p
        f.update(i["fields"])
        # print(f)
        n.append(f)

    print("fffffff")
    for i in n:
        print(i)
    t = n
    # print("aaaaaaaaaaaa")
    # t = [i["fields"].update({"pk": i["pk"]}) for i in t]
    # # b = [i["pk"] for i in t]
    # print("bbbbbbbbbbb")
    # print(t)
    # t = []

    try:
        t = [{k: ast.literal_eval(v)[0] for k, v in i.items()} for i in t]
    except ValueError:
        try:
            t = [{k: ast.literal_eval(v) for k, v in i.items()} for i in t]
        except ValueError:
            t = [{k: v for k, v in i.items()} for i in t]

    return t

    # return [i  i in Location.objects.all().iterator()]
