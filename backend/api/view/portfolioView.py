from django.http import JsonResponse
from rest_framework.views import APIView
from backend.api.comm.json_loader import colours_cfg
from backend.api.cqrs_q.portfolio import get_portfolios, get_portfolios_with_locations, delete_portfolio
from backend.api.cqrs_c.portfolio import create_or_update

class PortfolioView(APIView):

    def delete(self, request, name):
        print("PortfolioView delete")
        print(request.data)
        print("name to del", name)

        delete_portfolio(username=request.username, portfolio_name=name)

        response = {
            "auth": {
                "status": True,
                "access-token": request.access_token,
                "refresh-token": request.refresh_token
            },
            "payload": {
                "status": True
            }
        }
        return JsonResponse(response)

    def post(self, request):
        print("PortfolioView post")
        print(request.data)

        print(request.username)
        portfolio_name = request.data["currentName"]
        portfolio_new_name = request.data["newName"]
        portfolio_colour = request.data["colour"]

        create_or_update(
            request.username,
            portfolio_name,
            portfolio_new_name,
            portfolio_colour
        )

        response = {
            "auth": {
                "status": True,
                "access-token": request.access_token,
                "refresh-token": request.refresh_token
            },
            "payload": {

            }
        }
        return JsonResponse(response)

    def get(self, request):

        print("get for user")
        username = request.username
        print(username)

        portfolios = get_portfolios(username)
        print("portfolios", portfolios)
        print(80 * "-")
        print(type(portfolios))
        r = {}
        for i in portfolios:
            print(i)
            print(i.name)
            r[i.name] = {
                "newName": i.name,
                "oldName": i.name,
                "colour": i.colour
            }

        portfolio_locations = get_portfolios_with_locations(username)
        print(f"{portfolio_locations}")

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
                "portfolios":
                    r
                    # 0: {
                    #     "newName": "portfolio r",
                    #     "oldName": "portfolio r",
                    #     "colour": "bl"
                    # },
                    # 1: {
                    #     "newName": "portfolio 1fff",
                    #     "oldName": "portfolio 1fff",
                    #     "colour": "bdaasl"
                    # },
                    # 2: {
                    #     "newName": "portfolio 1eqedw",
                    #     "oldName": "portfolio 1eqedw",
                    #     "colour": "bl,w,"
                    # },

                    # "portfolio 1": {
                    #     "colour": "Black",
                    #     # locations
                    #     # "locations": {
                    #     #
                    #     # }
                    # },
                    # "portfolio 2": {
                    #     "colour": "Red"
                    # },
                    # "portfolio 3": {
                    #     "colour": "Maroon"
                    # }


            }
        }
        return JsonResponse(response)

