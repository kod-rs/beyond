import json

from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api import controller


class LocationView(APIView):

    def post(self, request) -> JsonResponse:
        """
        # TODO this, better
        Request has a json body structured as:
            {location_ids: [...]}
        returns:
            JsonResponse:
        """
        locations = json.loads(request.body)
        location_ids = locations.get('location_ids')
        locations = controller.location.get_locations_by_location_ids(
            location_ids)

        if not locations:
            return JsonResponse({'status': False})

        return JsonResponse({'status': True,
                             'locations': list(locations)})
