from django.http import JsonResponse

from backend.api.model.ip import IpCounter
import json

def pureDjangoView(request):
    # return HttpResponse("home page")
    t = IpCounter.objects.all()
    print(t)
    # print(json.loads(t))
    print("----")
    for i in t:
        print(i, i.ip, i.counter)
    # for i in t:
    #     print(i, i["ip"], i["counter"])
    print(t)
    # print(json.loads(t))
    return JsonResponse({"a": "b"})