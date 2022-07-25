from django.http import JsonResponse

from backend.api.model.ip import IpCounter

def pureDjangoView(request):
    # return HttpResponse("home page")
    t = IpCounter.objects.all()
    # for i in t:
    #     print(i, i["ip"], i["counter"])
    print(t)
    print(json(t))
    return JsonResponse({"a": "b"})