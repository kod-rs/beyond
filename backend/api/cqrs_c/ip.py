from backend.api.model.ip import IpCounter


def log_user_auth_attempt(ip):
    """
    counter++

    """

    i, _ = IpCounter.objects.get_or_create(
        ip=ip, defaults={"counter": 0}
    )
    i.counter += 1
    i.save()


def auth_user(ip):
    """
    reset counter to 0

    """

    i, _ = IpCounter.objects.get_or_create(
        ip=ip, defaults={"counter": 0}
    )
    i.save()
