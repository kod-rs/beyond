import json

from django.http import JsonResponse
from ipware import get_client_ip
from rest_framework import status

# from backend.api.view.error import ErrorView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from backend.api.authenticate import login, check_tokens
from backend.api.model.ip import IpCounter

# from django.db import models
#
# class Ip(models.Model):
#
#     ip = models.CharField(max_length=200)
#     counter = models.IntegerField()


class IpCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.max_brute_force_count = 500


    def check_username_password(self, username, password):
        print("username password")

        return login(username, password)["ok"]


        # if responseJson["ok"]:
        #     """all ok"""
        #
        #     if IpCounter.objects.filter(ip=ip):
        #         # if in db increment
        #         ip_entry = IpCounter.objects.get(ip=ip)
        #         print("in db", ip_entry, ip_entry.counter)
        #         ip_entry.counter = 1
        #         ip_entry.save()
        #     else:
        #         # else add with def val 1
        #         counter = 1
        #         ip_entry = IpCounter(ip=ip, counter=counter)
        #         print("not in db", ip_entry, ip_entry.counter)
        #         ip_entry.save()
        #
        #     # login can be made, user is logged in
        #     return True
        # else:
        #     """fcc++"""
        #     counter = None
        #
        #     if IpCounter.objects.filter(ip=ip):
        #         # if in db increment
        #         ip_entry = IpCounter.objects.get(ip=ip)
        #         print("in db", ip_entry, ip_entry.counter)
        #         ip_entry.counter += 1
        #         ip_entry.save()
        #         counter = ip_entry.counter
        #     else:
        #         # else add with def val 1
        #         counter = 1
        #         ip_entry = IpCounter(ip=ip, counter=counter)
        #         print("not in db", ip_entry, ip_entry.counter)
        #         ip_entry.save()
        #
        #     #
        #     return counter > 5
        #     # if counter > 5:
        #     #     return False
        #
        #     # print(Ip.objects.filter(ip=ip))
        #
        #         # todo else this is check for tokens
        #
        #         # FCC = false combination counter
        #
        #         # if user password combination not present -> FCC++ for this ip
        #
        #         # if access token or refresh token is not correct -> FCC++ for this ip
        #
        #         # if FCC == 5: deny
        #         # else continue
        #     #
        #     #     if ip == "127.0.0.1":
        #     #         print("ip blocked", ip)
        #     #         return JsonResponse({"ip blocked": True})
        #     #
        #     #     # We got the client's IP address
        #     #     if is_routable:
        #     #         print("public ip")
        #     #         # The client's IP address is publicly routable on the Internet
        #     #     else:
        #     #         print("private ip")
        #     # # The client's IP address is private

    def check_tokens(self, access_token, refresh_token):
        """"""
        print("todo other check ")
        return check_tokens(access_token, refresh_token)


    def __call__(self, request):


        print(80 * "-")
        print("ip check")
        ip, is_routable = get_client_ip(request)

        # if is_routable:
        #     print("public ip")
        #     # The client's IP address is publicly routable on the Internet
        # else:
        #     # The client's IP address is private
        #     print("private ip")

        # todo obfuscate response
        #   check https, refresh access token

        response = {
            "ip present": False,
            "brute force count exceeded": True,
            "user validated": False
        }

        if not ip:
            print("unable to get clients ip")
            return JsonResponse(response)
        response["ip present"] = True

        if self.check_max_count(ip):
            return JsonResponse(response)
        response["brute force count exceeded"] = False

        self.increment_db_counter(ip)

        is_validated = None

        if request.headers and ("username" in request.headers) and ("password" in request.headers):

            is_validated = self.check_username_password(request.headers["username"], request.headers["password"])

        elif  request.headers and ("access_token" in request.headers):
            print("access token")
            is_validated = self.check_tokens(request.headers["access_token"], "tmp")

        # todo ako nije usro onda je counter = 0

        print("is blocked", is_validated)

        if is_validated:
            return JsonResponse(response)

        else:

            response = self.get_response(request)

            # Code to be executed for each request/response after
            # the view is called.

            return response

        # if request.body:
        #     print("body", request.body)
        #     body = request.body.decode('utf-8')
        #     print("body utf decoded", body)
        #     body = json.loads(body)
        #     if body:
        #         if ("username" in body) and ("password" in body):
        #             print("check user pass")
        #             is_blocked = not self.check_username_password(body["username"], body["password"])
        #         elif "access_token" in body:
        #
        #             print("check access token")
        #             is_blocked = not self.handle_other(body["access_token"], "tmp")
        #
        #     else:
        #         print("no body after json")

        # else:
        #     print("no body")
        #

        #
        # if not is_blocked:
        #     """"""
        #     # handle if body does not contains required params for user - pass login
        #     # is_blocked = self.handle_other(request, ip, is_routable)
        #
        #
        # if is_blocked:
        #     return JsonResponse({"no ip": False, "brute force": True})
        #
        # else:
        #     response = self.get_response(request)
        #
        #     # Code to be executed for each request/response after
        #     # the view is called.
        #
        #     return response

        # if hasattr(request, "body"):
        #     print(f"{body=}")
        #     if not body:
        #         print("no user pass")
        #     body = json.loads(body)
        #     print(body)
        #
        #     print("this is post")
        #     return self.handle_post(request, ip, is_routable)

        # else:
        #     print("this is nto post")
        #     return self.handle_other(request, ip, is_routable)

        # # Order of precedence is (Public, Private, Loopback, None)
        #
        # response = self.get_response(request)
        #
        # # Code to be executed for each request/response after
        # # the view is called.
        #
        # return response

    def check_max_count(self, ip):
        if IpCounter.objects.filter(ip=ip):
            ip_obj = IpCounter.objects.get(ip=ip)
            print("current count", ip_obj.counter)
            return ip_obj.counter > self.max_brute_force_count
                # return response

    def increment_db_counter(self, ip):
        if IpCounter.objects.filter(ip=ip):
            # if in db increment
            ip_entry = IpCounter.objects.get(ip=ip)
            print("in db", ip_entry, ip_entry.counter)
            ip_entry.counter += 1
            ip_entry.save()
        else:
            # else add with def val 1
            counter = 1
            ip_entry = IpCounter(ip=ip, counter=counter)
            print("not in db", ip_entry, ip_entry.counter)
            ip_entry.save()
