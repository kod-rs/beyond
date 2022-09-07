import urllib.parse

from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.cqrs_c.portfolio import create_or_update, delete_portfolio
from backend.api.cqrs_q.portfolio import get_portfolios
from backend.api.view.comm import get_auth_ok_response_template


class PortfolioView(APIView):

    def delete(self, request, name):
        print("PortfolioView delete")

        # todo check
        delete_portfolio(username=request.username, portfolio_name=name)

        response = get_auth_ok_response_template(request)
        response["payload"]["status"] = True

        return JsonResponse(response)

    def post(self, request):
        print("PortfolioView post")

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

        response = get_auth_ok_response_template(request)
        response["payload"]["status"] = r
        return JsonResponse(response)

    def get(self, request):
        username = request.username
        portfolios = get_portfolios(username)

        r = {}

        for i in portfolios:
            hex_colour = i.colour[1:]
            pre_hex_colour = i.colour

            query = hex_colour
            t = urllib.parse.quote(query)

            r[i.name] = {
                "newName": i.name,
                "oldName": i.name,
                "colourName": i.colour,
                "colourHex": pre_hex_colour,
                "colourHexEncoded": t,
                # todo log session state
                "isExpanded": False
            }

        response = get_auth_ok_response_template(request)
        response["payload"]["status"] = True

        response["payload"]["portfolios"] = r
        response["payload"]["role"] = "role 1"

        return JsonResponse(response)
