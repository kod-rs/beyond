from django.http import JsonResponse
from rest_framework.views import APIView

from backend_old.api.cqrs_c.portfolio import create_portfolio
from backend_old.api.cqrs_c.portfolio import delete_portfolio
from backend_old.api.cqrs_c.portfolio import update_portfolio
from backend_old.api.cqrs_c.portfolio_colour_adapter import get_last_colour
from backend_old.api.cqrs_q.portfolio import get_all_portfolio
from backend_old.api.view.common import get_auth_ok_response_template


class PortfolioView(APIView):

    def patch(self, request, name):
        print("LocationsView patch", name)

        response = get_auth_ok_response_template(request)
        response["payload"] = update_portfolio(request.username,
                                               name,
                                               request.data)
        return JsonResponse(response)

    def delete(self, request, name):
        print("PortfolioView delete", name)

        response = get_auth_ok_response_template(request)
        response["payload"] = delete_portfolio(username=request.username,
                                               portfolio_name=name)
        return JsonResponse(response)

    def post(self, request, name):
        print("PortfolioView post", name)
        response = get_auth_ok_response_template(request)

        colour = request.data["colour"] if 'colour' in request.data else None

        response["payload"] = create_portfolio(request.username,
                                               name,
                                               colour=colour)
        return JsonResponse(response)

    def get(self, request, name=None):
        print(f"portfolio get {name=}")

        response = get_auth_ok_response_template(request)
        if name:
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
                colour = get_last_colour(request.username, i.name)
                colour["name"] = i.name
                colour["isExpanded"] = False
                r[count] = colour

            response = get_auth_ok_response_template(request)
            response["payload"]["status"] = True
            response["payload"]["portfolios"] = r
            response["payload"]["role"] = request.role
            return JsonResponse(response)
