from backend.api.model.colourHistory import ColourHistory
from backend.api.model.user import User
from django.utils import timezone


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
    # select * from api_user where username='a' and portfolio='a' order by timestamp_colour_change asc

    """
    select history_colour_id_id from api_user where username='a' and portfolio='a' order by timestamp_colour_change desc limit 1

    """

    ch, _ = ColourHistory.objects.update_or_create(
        colour_hex_value=colour_hex,
        defaults={"colour_hex_value": colour_hex}
    )
    ch.save()

    u = User.objects.filter(portfolio=portfolio,username=username).order_by('timestamp_colour_change').first()
    print(u.timestamp_colour_change)



    # print(u.query)
    # u = User.objects.create(
    #     portfolio=portfolio,
    #     username=username,
    #     history_colour_id=ch,
    #     timestamp_colour_change=timezone.now()
    # )
    # u.save()

    # if last

    # if ColourHistory.objects.filter(colour_hex_value=colour_hex).exists():
    #
    #     print("object exists")
    #
    #     ch = ColourHistory.objects.create(
    #         colour_hex_value=colour_hex
    #     )
    #
    #     ch.save()
    #
    #     u = User.objects.create(
    #        portfolio=portfolio,
    #         username=username,
    #         history_colour_id=ch,
    #         timestamp_colour_change=timezone.now()
    #     )
    #     u.save()
    #
    #     return True
    #     return {"new": True}
    # else:
    #     return {"new": False}

    # i, _ = ColourHistory.objects.update_or_create(
    #     colour_hex_value=colour_hex,
    #     defaults={"colour_hex_value": colour_hex}
    # )

    # return i.id


def get_history():
    print("return history")