import urllib.parse

from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.cqrs_c.portfolio import create_or_update, delete_portfolio, \
    update_portfolio, update_portfolio_colour, update_portfolio_name, update
from backend.api.cqrs_q.portfolio import get_portfolios
from backend.api.view.comm import get_auth_ok_response_template

#
# def update_portfolio_name(username, portfolio_name, portfolio_new_name):
#     pass


class PortfolioView(APIView):


    def patch(self, request, name):

        print("LocationsView patch", name)

        # portfolio_new_name = request.data["name"]
        # portfolio_colour = request.data["colour"]

        # print(request.data)

        p = {k:v for k,v in request.data.items() if k in ["name", "colour"]}


        update(request.username, name, p)

        # if "name" in request.data and "colour" in request.data:
        #     print("name, colour in data")
        #     portfolio_new_name = request.data["name"]
        #     portfolio_new_colour = request.data["colour"]
        #
        #     update_portfolio(request.username, name, portfolio_new_name, portfolio_new_colour)
        #
        # elif "name" in request.data:
        #     print("name in data")
        #     portfolio_new_name = request.data["name"]
        #
        #     update_portfolio_name(request.username, name, portfolio_new_name)
        #
        # elif "colour" in request.data:
        #     print("has new colour")
        #     portfolio_new_colour = request.data["colour"]
        #
        #     update_portfolio_colour(request.username, name, portfolio_new_colour)

        # r = update_portfolio(
        #     request.username,
        #     portfolio_name,
        #     portfolio_new_name,
        #     portfolio_colour
        # )

        response = get_auth_ok_response_template(request)
        # response["payload"]["status"] = r
        return JsonResponse(response)


    def delete(self, request, name):
        print("PortfolioView delete")

        # todo check
        delete_portfolio(username=request.username, portfolio_name=name)

        response = get_auth_ok_response_template(request)
        response["payload"]["status"] = True

        return JsonResponse(response)

    def post(self, request, name):
        print("PortfolioView post")

        # todo more descriptive message for showing in ui
        r = create_or_update(
            request.username,
            name,
            name,
            request.data["colour"]
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
                "name": i.name,
                "colour": pre_hex_colour,

                # "newName": i.name,
                # "oldName": i.name,
                # "colourName": "deleted",
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
