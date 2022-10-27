import json

from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api.view import common


class LocationView(APIView):

    def post(self, request) -> JsonResponse:
        breakpoint()
        pass
