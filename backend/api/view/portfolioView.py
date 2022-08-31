from django.http import JsonResponse
from rest_framework.views import APIView


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
                "colours": {
                    " color 1": "color 1 val",
                    "color 28": "c 2 val",
                    "color 23": "3 val",
                },
                "portfolios": {
                    "portfolio 1": {
                        "colour": "color 1"
                    },
                    "portfolio 2": {
                        "colour": "color 2"
                    },
                    "portfolio 3": {
                        "colour": "color 3"
                    }

                }
            }
        }

        return JsonResponse(response)

