from django.http import JsonResponse
from rest_framework.views import APIView
from backend.api.comm.json_loader import colours_cfg
from backend.api.cqrs_q.portfolio import get_portfolios, get_portfolios_with_locations, get_portfolio_names
from backend.api.cqrs_c.portfolio import create_or_update, delete_portfolio


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

        # todo more descriptive message for showing in ui
        r = create_or_update(
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
                "status": r
            }
        }
        return JsonResponse(response)

    def get(self, request):

        print(80 * "-")
        r = get_portfolio_names(request.username)
        print(r, "------")
        for i in r:
            print(i.name)

        print("get for user")
        username = request.username
        print(username)

        portfolios = get_portfolios(username)

        r = {}
        for i in portfolios:
            print(i)
            print(i.name)
            r[i.name] = {
                "newName": i.name,
                "oldName": i.name,
                "colour": i.colour,

                # todo log session state
                "isExpanded": False
            }

        portfolio_locations = get_portfolios_with_locations(username)
        print(f"{portfolio_locations=}")

        response = {
            "auth": {
                "status": True,
                "access-token": request.access_token,
                "refresh-token": request.refresh_token
            },
            "payload": {
                "role": "role 1",
                "colours": colours_cfg,
                "portfolios":r
            }
        }
        return JsonResponse(response)

