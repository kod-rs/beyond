import collections

from django.http import JsonResponse
from django.utils import timezone
from rest_framework.views import APIView

from backend_old.api.comm.constants import NOT_EXISTS
from backend_old.api.cqrs_q.portfolio import get_single_portfolio
from backend_old.api.model.consumption import consumptionValues, consumptionEntry
from backend_old.api.model.location import Location
from backend_old.api.view.common import get_auth_ok_response_template


#
def validate_actions(correct_actions, to_check_actions):
    return collections.Counter(correct_actions) == collections.Counter(
        to_check_actions)


class ConsumptionView(APIView):

    def get(self, request, portfolio, section, _type, options=None):
        print("consumption get")
        print(request.data)
        response = get_auth_ok_response_template(request)

        if not options:
            response["payload"] = get_consumption_log(request.username,
                                                      portfolio, section,
                                                      _type)
        elif options == "last":
            response["payload"] = get_consumption_last(request.username,
                                                       portfolio, section,
                                                       _type)
        return JsonResponse(response)

    def post(self, request, value):
        value = float(value)
        print(f"temp post {value=}")
        response = get_auth_ok_response_template(request)

        section = request.data["section"]
        _type = request.data["type"]

        portfolio = request.data["portfolio"]
        response["payload"] = add_consumption_value(request.username, value,
                                                    portfolio, section, _type)
        return JsonResponse(response)


def write_consumption_value(value):
    ch, _ = consumptionValues.objects.update_or_create(value=value,
                                                       defaults={
                                                           "value": value})
    ch.save()
    return ch


def is_location_consumption_entry_present(username, portfolio, section, _type):
    return consumptionEntry.objects.filter(
        section=section,
        type=_type,
        location__portfolio__username=username,
        location__portfolio__name=portfolio
    ).exists()


def get_location_consumption_adapter(username, portfolio, section, _type):
    print(f"{username=} {portfolio=}")
    if not is_location_consumption_entry_present(username, portfolio, section,
                                                 _type):
        return NOT_EXISTS

    return consumptionEntry.objects.filter(
        section=section, type=_type,
        location__portfolio__username=username,
        location__portfolio__name=portfolio)


def get_single_location(portfolio_object, section, _type):
    try:
        return {
            "exists": True,
            "content":
                Location.objects.get(portfolio=portfolio_object,
                                     section=section, type=_type)

        }
    except Location.DoesNotExist:
        return {"exists": False}


def get_consumption_last(username, portfolio, section, _type):
    print("todo")

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

    t = consumptionEntry.objects.filter(location=location_object) \
        .order_by('-timestamp') \
        .first()
    return {"status": True, "consumptionTimestamp": str(t.timestamp),
            "consumptionValue": str(t.value.value)}


def get_consumption_log(username, portfolio, section, _type):
    print("todo")

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

    t = consumptionEntry.objects.filter(location=location_object)

    return {"status": True,
            "result": {str(i.timestamp): str(i.value.value) for i in t}}


def add_consumption_value(username, value, portfolio, section, _type):
    # todo optimize using transaction

    consumption_value_object = write_consumption_value(value)
    print(consumption_value_object.value)

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

    u = consumptionEntry.objects.create(
        location=location_object,
        value=consumption_value_object,
        timestamp=timezone.now())
    u.save()
    return {"status": True}
