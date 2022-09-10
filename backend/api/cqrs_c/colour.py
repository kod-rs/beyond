
from backend.api.model.colourHistory import ColourHistory
from backend.api.model.user import User
from django.utils import timezone

from django.core import serializers

def add_colour_to_user(portfolio, username, history_colour_id,timestamp_colour_change):
    i = User.objects.create(
        portfolio=portfolio,
        username=username,
        history_colour_id=history_colour_id,
        timestamp_colour_change=timestamp_colour_change
    )
    i.save()
    print("saved")

def clear_history(username, portfolio):
    User.objects.filter(username=username, portfolio=portfolio).delete()

def add_colour_to_log(username, portfolio, colour_hex):
    # select * from api_user where username='a' and portfolio='a' order by timestamp_colour_change asc

    """
    select history_colour_id_id from api_user where username='a' and portfolio='a' order by timestamp_colour_change desc limit 1

    todo rewrite with this
        insert into api_user (id, portfolio, username, history_colour_id_id, timestamp_colour_change) select 14, 'a', 'a', 3, '2022-09-08 18:58:09.432646+02' where (select history_colour_id_id from api_user where username='a' and portfolio='a' order by timestamp_colour_change desc limit 1) != 4;

    """

    ch, _ = ColourHistory.objects.update_or_create(
        colour_hex_value=colour_hex,
        defaults={"colour_hex_value": colour_hex}
    )
    ch.save()

    if User.objects\
        .filter(portfolio=portfolio,username=username).exists():

        u = User\
            .objects\
            .filter(portfolio=portfolio,username=username)\
            .order_by('-timestamp_colour_change')\
            .first()

        if ch.id == u.history_colour_id_id:
            print("this is last entry in db, nothing is changed")
            return

    print("cleanup")

    User\
        .objects\
        .filter(
            username=username,
            portfolio=portfolio,
            history_colour_id=ch.id
        )\
        .delete()


    print("new selected, changing")
    u = User.objects.create(
        portfolio=portfolio,
        username=username,
        history_colour_id=ch,
        timestamp_colour_change=timezone.now()
    )
    u.save()

    count = User \
        .objects \
        .filter(portfolio=portfolio, username=username)\
        .values("history_colour_id_id")\
        .distinct()\
        .count()
    print(f"{count=}")

    if count > 10:
        print("delete last")
        User\
            .objects\
            .filter(portfolio=portfolio,username=username)\
            .order_by('timestamp_colour_change')\
            .first().delete()
    # print(count.query)




    # if count == 11:
    #     print("deleting last")
    #     # .select_related("history_colour_id")

        # return t

    # print("added", ch.id)
    # print("last", u.history_colour_id_id)
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