from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.cqrs_c.portfolio_colour_adapter import \
    delete_portfolio_colour_entries, get_all_colours, get_last_colour, \
    add_color_to_log
from backend.api.view.common import get_auth_ok_response_template


class ColourView(APIView):

    def delete(self, request, name):
        print(f"colour delete {name=}", request.data)

        response = get_auth_ok_response_template(request)
        response["payload"] = delete_portfolio_colour_entries(request.username, name)
        return JsonResponse(response)

    def get(self, request, name):
        print(f"colour get {name=} {request.data=}")
        response = get_auth_ok_response_template(request)

        if not request.data:
            response["payload"] = get_all_colours(request.username, name)

        elif request.data["options"] == "last":
            print("last")
            response["payload"] = get_last_colour(request.username, name)

        return JsonResponse(response)

    def post(self, request, name):
        print(f"colour post {name=}")
        response = get_auth_ok_response_template(request)

        portfolio = request.data["portfolio"]
        response["payload"] =add_color_to_log(request.username, portfolio, name)
        return JsonResponse(response)
