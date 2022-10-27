from django.http import JsonResponse


def false_status(response_type: str, msg: str) -> JsonResponse:
    return JsonResponse({
        'type': response_type,
        'status': False,
        'message': msg})
