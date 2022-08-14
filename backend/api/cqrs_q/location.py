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
        n.append(f)

    t = n

    try:
        t = [{k: ast.literal_eval(v)[0] for k, v in i.items()} for i in t]
    except ValueError:
        try:
            t = [{k: ast.literal_eval(v) for k, v in i.items()} for i in t]
        except ValueError:
            t = [{k: v for k, v in i.items()} for i in t]

    return t

def get_all_by_username(username):
    t = serializers.serialize('json', Location.objects.filter(username=username))
    t = json.loads(t)
    print(t)

    n = []
    for i in t:
        f = {}
        p = i["pk"]
        f["pk"] = p
        f.update(i["fields"])
        del f["username"]
        n.append(f)

    t = n

    try:
        t = [{k: ast.literal_eval(v)[0] for k, v in i.items()} for i in t]
    except ValueError:
        try:
            t = [{k: ast.literal_eval(v) for k, v in i.items()} for i in t]
        except ValueError:
            t = [{k: v for k, v in i.items()} for i in t]

    return t
