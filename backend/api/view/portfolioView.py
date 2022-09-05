from django.http import JsonResponse
from rest_framework.views import APIView
from backend.api.comm.json_loader import colours_cfg
from backend.api.cqrs_q.portfolio import get_portfolio

class PortfolioView(APIView):

    def get(self, request):

        print("get for user")
        username = request.username
        print(username)

        portfolios = get_portfolio(username)
        print("portfolios", portfolios)

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
                        "colour": "Black",
                        # locations
                        # "locations": {
                        #
                        # }
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

