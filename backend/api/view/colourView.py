from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.cqrs_c.portfolio_colour_adapter import \
    delete_portfolio_colour_entries, get_all_colours, get_last_colour, \
    add_colour_to_log
from backend.api.view.comm import get_auth_ok_response_template


class ColourView(APIView):

    def delete(self, request, name):
        print(f"colour delete {name=}", request.data)
        # de
        # portfolio = request.data["portfolio"]
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

        print(response)


        # t = get_colour_log(request.username, name)
        #
        # r = {
        #     str(i.timestamp):
        #         i.colour.colour for i in t
        # }

        # response["payload"]["status"] = True
        return JsonResponse(response)

    def post(self, request, name):
        print(f"colour post {name=}")
        # print(request.data)
        response = get_auth_ok_response_template(request)

        portfolio = request.data["portfolio"]
        # colour_hex = request.data["colourHex"]
        response["payload"] =add_colour_to_log(request.username, portfolio, name)
         # response

        return JsonResponse(response)
