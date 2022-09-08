from backend.api.cqrs_q.portfolio import get_portfolio
from backend.api.model.colourHistory import ColourHistory
from backend.api.model.user import User


def add_colour_to_user(portfolio, username, history_colour_id,timestamp_colour_change):
    i = User.objects.create(
        portfolio=portfolio,
        username=username,
        history_colour_id=history_colour_id,
        timestamp_colour_change=timestamp_colour_change
    )
    i.save()
    print("saved")

def add_colour_to_log(username, portfolio, colour_hex):
    print(username, portfolio, colour_hex)
    # p = get_portfolio(portfolio)

    i, _ = ColourHistory.objects.update_or_create(
         defaults={"colour_hex_value": colour_hex}
    )
    i.save()

    return i.id

    # l = Colour.objects.create(
    #     colour_hex_value=colour_hex
    # )
    #
    # l.save()

    return True

def get_history():
    print("return history")