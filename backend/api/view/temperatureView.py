import collections

from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.comm.comm import bytes_to_json
from backend.api.cqrs_c.location import add, delete, update
from backend.api.cqrs_q.location import get_user_portfolio
from backend.api.cqrs_q.portfolio import get_single_portfolio
from backend.api.mode.type_validator import _check_request_data
from backend.api.model.location import Location
from backend.api.model.temperature import TemperatureValues, TemperatureEntry
from backend.api.view.comm import get_auth_ok_response_template


#
def validate_actions(correct_actions, to_check_actions):
    return collections.Counter(correct_actions) == collections.Counter(
        to_check_actions)


class TemperatureView(APIView):
    # def patch(self, request, portfolio, section, _type):
    #     print("LocationsView patch")
    #
    #     response = get_auth_ok_response_template(request)
    #     response["payload"]["status"] = update(request.username, portfolio, section, _type, request.data)
    #     return JsonResponse(response)
    #
    #
    # def delete(self, request, portfolio, section, _type):
    #     print("delete single", portfolio, section, _type)
    #
    #     response = get_auth_ok_response_template(request)
    #
    #     r = delete(request.username,portfolio, section, _type)
    #
    #     response["payload"]["status"] = r
    #     return JsonResponse(response)

    # def get(self, request, portfolio=None,section=None, _type=None):
    #     print("location get")
    #     response = get_auth_ok_response_template(request)
    #
    #     if portfolio and section and _type:
    #         """fetch data for graphs"""
    #
    #
    #     elif portfolio and not section and not _type:
    #         print(f"get all locations for {portfolio=}")
    #
    #         username_locations = get_user_portfolio(request.username, portfolio)
    #
    #         r = {}
    #         j = 0
    #         for i in username_locations:
    #             r[j] = {
    #                 "section": i.section,
    #                 "type": i.type,
    #                 # todo refactor to latitude & longitude
    #                 "lat": i.latitude,
    #                 "lon": i.longitude,
    #             }
    #
    #             j += 1
    #
    #         payload = {"status": True, "content": r}
    #         result = payload
    #
    #         response["payload"] = result
    #         return JsonResponse(response)
    #
    #     print("todo")
    #
    #     print(f"locations get {portfolio=} {section=} {_type=}")
    #
    #     # response = get_auth_ok_response_template(request)
    #     #
    #     # username_locations = get_user_portfolio(request.username,portfolio)
    #     #
    #     # r = {}
    #     # j = 0
    #     # for i in username_locations:
    #     #     r[j] = {
    #     #         "section": i.section,
    #     #         "type": i.type,
    #     #         # todo refactor to latitude & longitude
    #     #         "lat": i.latitude,
    #     #         "lon": i.longitude,
    #     #     }
    #     #
    #     #     j += 1
    #     #
    #     # payload = {"status": True, "content": r}
    #     # result = payload
    #
    #     # response["payload"] = result
    #     return JsonResponse(response)

    def get(self, request):
        print("temperature get")
        print(request.data)
        response = get_auth_ok_response_template(request)
        # todo extract last to constant

        # print(request.body)

        section = request.data["section"]
        _type = request.data["type"]
        portfolio = request.data["portfolio"]

        if not "options" in request.data:
            # portfolio = request.data["portfolio"]

            response["payload"] =get_temperature_log(request.username, portfolio, section, _type)
        elif request.data["options"] == "last":
            response["payload"] =get_temperature_last(request.username, portfolio, section, _type)
        # mperature_last(username, portfolio, section, _type)

        return JsonResponse(response)

    def post(self, request, value):
        value = float(value)
        print(f"temp post {value=}")
        response = get_auth_ok_response_template(request)

        # portfolio = request.data["portfolio"]
        section = request.data["section"]
        _type = request.data["type"]

        portfolio = request.data["portfolio"]
        response["payload"] =add_temperature_value(request.username, value, portfolio, section, _type)
        return JsonResponse(response)


def write_temperature_value(value):
    ch, _ = TemperatureValues.objects.update_or_create(
        value=value,
        defaults={"value": value}
    )
    ch.save()
    return ch


def is_location_temperature_entry_present(username, portfolio, section, _type):
    return TemperatureEntry.objects.filter(
        section=section,
        type=_type,
        location__portfolio__username=username,
        location__portfolio__name=portfolio
    ).exists()


def get_location_temperature_adapter(username, portfolio, section, _type):
    print(f"{username=} {portfolio=}")
    if not is_location_temperature_entry_present(username,portfolio,section,_type):
        return NOT_EXISTS

    return TemperatureEntry.objects.filter(section=section, type=_type, location__portfolio__username=username,
                                                 location__portfolio__name=portfolio)



from backend.api.comm.constants import max_temperature_log, NOT_EXISTS, EXISTS
from django.utils import timezone


def get_single_location(portfolio_object, section, _type):
    try:
        return {
            "exists": True,
            "content":
                Location.objects.get(portfolio=portfolio_object, section=section, type=_type)

        }
    except Location.DoesNotExist:
        return {"exists": False}

def get_temperature_last(username, portfolio, section, _type):
    print("todo")
    r = {"status": False}

    portfolio_object = get_single_portfolio(username, portfolio)
    if portfolio_object["exists"]:
        portfolio_object = portfolio_object["content"]
    else:
        return {"err": "portfolio not exists", "status": False}

    location_object = get_single_location(portfolio_object, section, _type)
    if location_object["exists"]:
        location_object = location_object["content"]
    else:
        return {"err": "location not exists", "status": False}

    t = TemperatureEntry.objects.filter(location=location_object)\
        .order_by('-timestamp') \
            .first()
    return {"status": True, "temperatureTimestamp": str(t.timestamp), "temperatureValue": str(t.value.value)}


def get_temperature_log(username,  portfolio, section, _type):
    print("todo")
    r = {"status": False}

    portfolio_object = get_single_portfolio(username, portfolio)
    if portfolio_object["exists"]:
        portfolio_object = portfolio_object["content"]
    else:
        return {"err": "portfolio not exists", "status": False}

    location_object = get_single_location(portfolio_object, section, _type)
    if location_object["exists"]:
        location_object = location_object["content"]
    else:
        return {"err": "location not exists", "status": False}

    t = TemperatureEntry.objects.filter(location=location_object)

    return {"status": True,
            "result": {str(i.timestamp): str(i.value.value) for i in t}}


def add_temperature_value(username, value, portfolio, section, _type):
    r = {"status": False}
    # todo optimize using transaction

    temperature_value_object = write_temperature_value(value)
    print(temperature_value_object.value)

    portfolio_object = get_single_portfolio(username, portfolio)
    if portfolio_object["exists"]:
        portfolio_object = portfolio_object["content"]
    else:
        return {"err": "portfolio not exists", "status": False}

    location_object = get_single_location(portfolio_object, section, _type)
    if location_object["exists"]:
        location_object = location_object["content"]
    else:
        return {"err": "location not exists", "status": False}

    u = TemperatureEntry.objects.create(
        location =location_object,
        value=temperature_value_object,
        timestamp=timezone.now()
    )
    u.save()
    # todo     while current_time - constant_time > last_entry: delete

    return {"status": True}