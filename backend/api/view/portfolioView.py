import urllib.parse

from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.cqrs_c.portfolio import  delete_portfolio, \
    update_portfolio, create_portfolio
from backend.api.cqrs_q.portfolio import get_all_portfolio, get_single_portfolio
from backend.api.view.comm import get_auth_ok_response_template

from backend.api.comm.constants import EXISTS,CREATED

class PortfolioView(APIView):

    def patch(self, request, name):
        print("LocationsView patch", name)

        response = get_auth_ok_response_template(request)
        response["payload"] = update_portfolio(request.username, name, request.data)
        return JsonResponse(response)

    def delete(self, request, name):
        print("PortfolioView delete", name)

        response = get_auth_ok_response_template(request)
        response["payload"] = delete_portfolio(username=request.username, portfolio_name=name)
        return JsonResponse(response)

    def post(self, request, name):
        print("PortfolioView post", name)
        response = get_auth_ok_response_template(request)

        response["payload"]= create_portfolio(request.username, name, request.data["colour"])
        return JsonResponse(response)

    def get(self, request, name=None):
        print(f"portfolio get {name=}")

        response = get_auth_ok_response_template(request)
        if name:
            # todo
            # p = get_single_portfolio(request.username, name)
            print("not implemented")
            response["payload"]["status"] = False
            response["payload"]["description"] = "not implemented"
            return JsonResponse(response)

        else:


            c = get_all_portfolio(request.username)

            if not c["exists"]:
                response["payload"]["status"] = False
                return JsonResponse(response)

            portfolios = c["payload"]
            r = {}

            for count, i in enumerate(portfolios):
                hex_colour = i.colour[1:]

                query = hex_colour
                t = urllib.parse.quote(query)

                r[count] = {
                    "name": i.name,
                    "colour": i.colour,
                    # todo remove
                    "colourHexEncoded": t,
                    # todo log session state
                    "isExpanded": False
                }

            response = get_auth_ok_response_template(request)
            response["payload"]["status"] = True

            response["payload"]["portfolios"] = r

            response["payload"]["role"] = request.role

            return JsonResponse(response)
