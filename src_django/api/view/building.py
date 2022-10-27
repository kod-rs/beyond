import json

from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api.view import common

class BuildingView(APIView):
    def __init__(self):
        super().__init__()
        self._response_type = 'get_buildings_by_user_id_response'

    def post(self, request) -> JsonResponse:
        credentials = json.loads(request.body)
        reason = credentials.get('type')
        username = credentials.get('username')
        password = credentials.get('password')

