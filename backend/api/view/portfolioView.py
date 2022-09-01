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
                    "Black": {
                        "name": "black",
                        "hex": "#000000"
                    },
                    "Red": {
                        "name": "red",
                        "hex": "#FF0000"
                    },
                    "Maroon": {
                        "name": "Maroon",
                        "hex": "#800000"
                    },
                    "yellow": {
                        "name": "yellow",
                        "hex": "#DFFF00"
                    }
                },
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

