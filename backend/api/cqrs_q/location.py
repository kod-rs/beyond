import ast
import json

from backend.api.model.location import Location
from django.core import serializers
from django.forms.models import model_to_dict
import json
from ast import parse

def get_all():

    t = serializers.serialize('json', Location.objects.all())
    t = json.loads(t)
    t = [i["fields"] for i in t]

    t = [{k: ast.literal_eval(v) for k,v in i.items()} for i in t]


    return t

    # return [i  i in Location.objects.all().iterator()]

