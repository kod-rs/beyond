import urllib.parse

from django.http import JsonResponse
from rest_framework.views import APIView

# from backend.api.cqrs_c.colour import get_last_colour
from backend.api.cqrs_c.portfolio import  delete_portfolio, \
    update_portfolio, create_portfolio
from backend.api.cqrs_c.portfolio_colour_adapter import get_last_colour
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

        colour = None
        if "colour" in request.data:
            colour = request.data["colour"]

        response["payload"]= create_portfolio(request.username, name, colour=colour)
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
                # print(count, i)



                colour =  get_last_colour(request.username, i.name)
                # print(f"{colour=}")
                # colour["a"] = "b"
                colour["name"] = i.name
                #  # # todo log session state

                colour["isExpanded"] = False
                # print(f"{colour=}")/

                # if colour["status"]:
                #     colour = colour["colour"]
                #     colour_timestamp = colour

                # hex_colour = i.colour[1:]

                # query = hex_colour
                # t = urllib.parse.quote(query)

                # # r[count] = \
                # t = {
                #     "name": i.name,
                #
                #     # "colour": i.colour,
                #     # # todo remove
                #     # "colourHexEncoded": t,
                #     # # todo log session state
                #     "isExpanded": False
                # }
                # r[count] = {key: value for (key, value) in
                #                (t.items() + colour.items())}
                r[count] = colour

            response = get_auth_ok_response_template(request)
            response["payload"]["status"] = True

            response["payload"]["portfolios"] = r

            response["payload"]["role"] = request.role

            return JsonResponse(response)
