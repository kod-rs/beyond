import ast
import json

from django.core import serializers

from backend.api.model.csrf import CSRF


def get_all():
    t = serializers.serialize('json', CSRF.objects.all())
    t = json.loads(t)

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


def get_by_ip(ip):
    if CSRF.objects.filter(ip=ip).exists():
        entry = CSRF.objects.get(ip=ip)
        return entry
