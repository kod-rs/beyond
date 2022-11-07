from django.http import JsonResponse
import json


def false_status(response_type: str, msg: str) -> JsonResponse:
    return JsonResponse({
        'type': response_type,
        'status': False,
        'message': msg})


def json_decode(request_body: bytes) -> dict:
    try:
        return json.loads(request_body)
    except Exception as e:
        print(f'Exception while decoding the body={e}')
        return {}
