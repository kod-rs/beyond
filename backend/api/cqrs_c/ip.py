from backend.api.model.ip import IpCounter


def log_user_auth_attempt(ip):
    """
    counter++

    """

    if IpCounter.objects.filter(ip=ip):
        ip_entry = IpCounter.objects.get(ip=ip)
        ip_entry.counter += 1
        ip_entry.save()
    else:
        ip_entry = IpCounter(ip=ip, counter=1)
        ip_entry.save()


def auth_user(ip):
    """
    reset counter to 0

    """

    if IpCounter.objects.filter(ip=ip):
        ip_entry = IpCounter.objects.get(ip=ip)
        ip_entry.counter = 0
        ip_entry.save()
    else:
        ip_entry = IpCounter(ip=ip, counter=0)
        ip_entry.save()
