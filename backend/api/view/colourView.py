from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.cqrs_c.colour import add_colour_to_log, clear_history
from backend.api.cqrs_q.user import get_colour_log
from backend.api.view.comm import get_auth_ok_response_template
class ColourView(APIView):

    def delete(self, request, abc):
        clear_history(request.username, abc)
        response = get_auth_ok_response_template(request)
        return JsonResponse(response)

    def get(self, request, abc):
        print("colour get")

        t = get_colour_log(request.username, abc)

        r = {
            str(i.timestamp_colour_change): i.history_colour_id.colour_hex_value for i in t
        }

        response = get_auth_ok_response_template(request)
        response["payload"]["status"] = True
        response["payload"]["value"] = r
        return JsonResponse(response)

    def post(self, request):
        print("colour post")
        response = get_auth_ok_response_template(request)

        portfolio = request.data["portfolio"]
        colour_hex = request.data["colourHex"]
        r = add_colour_to_log(request.username, portfolio, colour_hex)
        print(r)
        print("")

        """
        history
        user 
        timestamp
        name
        
        triger on insert  brisi starije
        
        -u1,0,a
        u1,1,a
        u1,2,a
        u1,3,a
        
        """

        return JsonResponse(response)
