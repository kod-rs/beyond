from django.http import JsonResponse
from rest_framework.views import APIView
from django.utils import timezone

from backend.api.cqrs_c.colour import add_colour_to_log, add_colour_to_user
from backend.api.view.comm import get_auth_ok_response_template
# from backend
class ColourView(APIView):

    def get(self, request, abc):

        print("colour get")
        print("a", request.username)
        print("b", abc)
        # portfolio_name = t
        print(request.username, abc)

        response = get_auth_ok_response_template(request)
        return JsonResponse(response)

    def post(self, request):
        print("colour post")
        response = get_auth_ok_response_template(request)

        portfolio = request.data["portfolio"]
        colour_hex = request.data["colourHex"]
        r = add_colour_to_log(request.username, portfolio, colour_hex)
        print(r)
        print("")

        r = add_colour_to_user(
            portfolio=portfolio,
            username=request.username,
            history_colour_id=r,
            timestamp_colour_change=timezone.now()
        )
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


    # def get(self, request):
    #     print("colour get")
    #     response = get_auth_ok_response_template(request)
    #
    #     #
    #     # response = {
    #     #     "auth": {
    #     #         "status": True,
    #     #         "access-token": request.access_token,
    #     #         "refresh-token": request.refresh_token
    #     #     },
    #     #     "payload": {
    #     #         "page": "index"
    #     #     }
    #     # }
    #     #
    #     # return JsonResponse(response)
    #
    #     # response["payload"]["status"] = True
    #
    #     # response["payload"] = "result"
    #     return JsonResponse(response)
