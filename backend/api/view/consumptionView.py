import collections

from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.comm.comm import bytes_to_json
from backend.api.cqrs_c.location import add, delete, update
from backend.api.cqrs_q.location import get_user_portfolio
from backend.api.cqrs_q.portfolio import get_single_portfolio
from backend.api.mode.type_validator import _check_request_data
from backend.api.model.location import Location
from backend.api.model.consumption import consumptionValues, consumptionEntry
from backend.api.view.comm import get_auth_ok_response_template


#
def validate_actions(correct_actions, to_check_actions):
    return collections.Counter(correct_actions) == collections.Counter(
        to_check_actions)


class ConsumptionView(APIView):


    def get(self, request, portfolio, section, _type, options=None):
        print("consumption get")
        print(request.data)
        # print(request.body)
        response = get_auth_ok_response_template(request)
        # todo extract last to constant


        # section = request.data["section"]
        # _type = request.data["type"]
        # portfolio = request.data["portfolio"]

        if not options:
            response["payload"] =get_consumption_log(request.username, portfolio, section, _type)
        elif options == "last":
            response["payload"] =get_consumption_last(request.username, portfolio, section, _type)
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
        response["payload"] =add_consumption_value(request.username, value, portfolio, section, _type)
        return JsonResponse(response)


def write_consumption_value(value):
    ch, _ = consumptionValues.objects.update_or_create(
        value=value,
        defaults={"value": value}
    )
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
    if not is_location_consumption_entry_present(username,portfolio,section,_type):
        return NOT_EXISTS

    return consumptionEntry.objects.filter(section=section, type=_type, location__portfolio__username=username,
                                                 location__portfolio__name=portfolio)



from backend.api.comm.constants import max_consumption_log, NOT_EXISTS, EXISTS
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

def get_consumption_last(username, portfolio, section, _type):
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

    t = consumptionEntry.objects.filter(location=location_object)\
        .order_by('-timestamp') \
            .first()
    return {"status": True, "consumptionTimestamp": str(t.timestamp), "consumptionValue": str(t.value.value)}


def get_consumption_log(username,  portfolio, section, _type):
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

    t = consumptionEntry.objects.filter(location=location_object)

    return {"status": True,
            "result": {str(i.timestamp): str(i.value.value) for i in t}}


def add_consumption_value(username, value, portfolio, section, _type):
    r = {"status": False}
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
        location =location_object,
        value=consumption_value_object,
        timestamp=timezone.now()
    )
    u.save()
    # todo     while current_time - constant_time > last_entry: delete

    return {"status": True}