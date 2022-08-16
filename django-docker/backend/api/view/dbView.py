from django.http import JsonResponse

from backend.api.model.ip import IpCounter


def pureDjangoView(request):
    _ = IpCounter.objects.all()
    return JsonResponse({"a": "b"})
