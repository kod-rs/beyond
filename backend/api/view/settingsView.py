
from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.model.user import User
from backend.api.view.comm import get_auth_ok_response_template


class SettingsView(APIView):

    def get(self, request):
        response = get_auth_ok_response_template(request)

        s = get_settings(username=request.username)
        if s["exists"]:
            s = s["content"]

            print("settings for user", s)
            # print(s.zoom_user_location)

            response["payload"] = {
                "status": True,
                "zoomUserLocation": s.zoomUserLocation,
            }

        else:
            response["payload"] = {
                "status": False,
            }

        return JsonResponse(response)

    def post(self, request):
        print(request.data)

        # zoomUserLocation
        update_settings(request.username, request.data)

        response = get_auth_ok_response_template(request)
        response["payload"]["status"] = True
        return JsonResponse(response)

def get_settings(username):
    try:
        return {
            "exists": True,
            "content":
                User.objects.get(username=username)

        }
    except User.DoesNotExist:
        return {"exists": False}

def update_settings(username, settings):


    j = {k:v for k,v in settings.items()}
    j["username"] = username
    i, _ = User.objects.update_or_create(
        username=username,
         defaults=j
    )
    i.save()