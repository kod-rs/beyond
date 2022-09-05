from django.http import JsonResponse
from rest_framework.views import APIView
from backend.api.comm.json_loader import colours_cfg
class PortfolioView(APIView):

    def get(self, request):

        response = {
            "auth": {
                "status": True,
                "access-token": request.access_token,
                "refresh-token": request.refresh_token
            },
            "payload": {
                "role": "role 1",
                "colours": colours_cfg
                ,
                "portfolios": {
                    "portfolio 1": {
                        "colour": "Black"
                    },
                    "portfolio 2": {
                        "colour": "Red"
                    },
                    "portfolio 3": {
                        "colour": "Maroon"
                    }

                }
            }
        }
        return JsonResponse(response)

