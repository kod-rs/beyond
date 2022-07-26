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
        # self.blocked_response = ErrorView

    def handle_post(self, request, ip, routable):
        """
        assumption user password post from login

        """

        print("post type")
        # print(type(request))
        # print(ip, type(ip))

        counter = 6
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

        print("counter", counter, type(counter))
        if counter > 50:
            print("max brute f")
            return False

        # todo if body exist then this is login
        body = request.body.decode('utf-8')
        body = json.loads(body)
        print(body)

        responseJson = login(**body)
        # print("----")
        # print(responseJson)

        if responseJson["ok"]:
            """all ok"""

            if IpCounter.objects.filter(ip=ip):
                # if in db increment
                ip_entry = IpCounter.objects.get(ip=ip)
                print("in db", ip_entry, ip_entry.counter)
                ip_entry.counter = 1
                ip_entry.save()
            else:
                # else add with def val 1
                counter = 1
                ip_entry = IpCounter(ip=ip, counter=counter)
                print("not in db", ip_entry, ip_entry.counter)
                ip_entry.save()

            # login can be made, user is logged in
            return True
        else:
            """fcc++"""
            counter = None

            if IpCounter.objects.filter(ip=ip):
                # if in db increment
                ip_entry = IpCounter.objects.get(ip=ip)
                print("in db", ip_entry, ip_entry.counter)
                ip_entry.counter += 1
                ip_entry.save()
                counter = ip_entry.counter
            else:
                # else add with def val 1
                counter = 1
                ip_entry = IpCounter(ip=ip, counter=counter)
                print("not in db", ip_entry, ip_entry.counter)
                ip_entry.save()

            #
            return counter > 5
            # if counter > 5:
            #     return False

            # print(Ip.objects.filter(ip=ip))

                # todo else this is check for tokens

                # FCC = false combination counter

                # if user password combination not present -> FCC++ for this ip

                # if access token or refresh token is not correct -> FCC++ for this ip

                # if FCC == 5: deny
                # else continue
            #
            #     if ip == "127.0.0.1":
            #         print("ip blocked", ip)
            #         return JsonResponse({"ip blocked": True})
            #
            #     # We got the client's IP address
            #     if is_routable:
            #         print("public ip")
            #         # The client's IP address is publicly routable on the Internet
            #     else:
            #         print("private ip")
            # # The client's IP address is private

    def handle_other(self, request, ip, routable):
        """"""
        print("todo other check ")
        return check_tokens("access token", "refresh token")


    def __call__(self, request):
        # response = self.get_response(request)
        #
        # # Code to be executed for each request/response after
        # # the view is called.
        #
        # return response
        # return JsonResponse({"no ip": True})

        print("ip check")
        ip, is_routable = get_client_ip(request)

        # if is_routable:
        #     print("public ip")
        #     # The client's IP address is publicly routable on the Internet
        # else:
        #     # The client's IP address is private
        #     print("private ip")

        if not ip:
            print("unable to get clients ip")
            return JsonResponse({"no ip": True})

        # return JsonResponse({"a": True})


        # todo if ip blocklisted return

        is_blocked = None

        if hasattr(request, "body"):
            body = request.body.decode('utf-8')
            body = json.loads(body)
            # print(body, type(body))
            # print(body["username"])
            # print("username" in body)
            # # print(body[0])
            # print(body ==  True)
            # print(hasattr(body, "username"))
            # print(hasattr(body, "passsword"))

            if body and ("username" in body) and ("password" in body):
                print("check user pass")
                is_blocked = not self.handle_post(request, ip, is_routable)

        if not is_blocked:

            # handle if body does not contains required params for user - pass login
            is_blocked = self.handle_other(request, ip, is_routable)

        if is_blocked:
            return JsonResponse({"no ip": False, "brute force": True})

        else:
            response = self.get_response(request)

            # Code to be executed for each request/response after
            # the view is called.

            return response

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
