from django.utils import timezone

from backend.api.model.colourHistory import ColourHistory
from backend.api.model.user import User


def add_colour_to_user(
        portfolio, username, history_colour_id, timestamp_colour_change):
    i = User.objects.create(
        portfolio=portfolio,
        username=username,
        history_colour_id=history_colour_id,
        timestamp_colour_change=timestamp_colour_change
    )
    i.save()


def clear_history(username, portfolio):
    User.objects.filter(username=username, portfolio=portfolio).delete()


def add_colour_to_log(username, portfolio, colour_hex):
    # todo rewrite with this
    #     insert into api_user (id, portfolio, username, history_colour_id_id, timestamp_colour_change) select 14, 'a', 'a', 3, '2022-09-08 18:58:09.432646+02' where (select history_colour_id_id from api_user where username='a' and portfolio='a' order by timestamp_colour_change desc limit 1) != 4;

    # todo optimize using transaction

    ch, _ = ColourHistory.objects.update_or_create(
        colour_hex_value=colour_hex,
        defaults={"colour_hex_value": colour_hex}
    )
    ch.save()

    if User.objects \
            .filter(portfolio=portfolio, username=username).exists():

        u = User \
            .objects \
            .filter(portfolio=portfolio, username=username) \
            .order_by('-timestamp_colour_change') \
            .first()

        if ch.id == u.history_colour_id_id:
            print("this is last entry in db, nothing is changed")
            return

    User \
        .objects \
        .filter(
        username=username,
        portfolio=portfolio,
        history_colour_id=ch.id
    ) \
        .delete()

    u = User.objects.create(
        portfolio=portfolio,
        username=username,
        history_colour_id=ch,
        timestamp_colour_change=timezone.now()
    )
    u.save()

    count = User \
        .objects \
        .filter(portfolio=portfolio, username=username) \
        .values("history_colour_id_id") \
        .distinct() \
        .count()

    if count > 10:
        User \
            .objects \
            .filter(portfolio=portfolio, username=username) \
            .order_by('timestamp_colour_change') \
            .first().delete()
