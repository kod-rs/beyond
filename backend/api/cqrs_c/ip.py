from backend.api.model.ip import IpCounter


def log_user_auth_atempt(ip):
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


def auth_user(ip, count):
    """reset user """

    if IpCounter.objects.filter(ip=ip):
        # if in db increment
        ip_entry = IpCounter.objects.get(ip=ip)
        print("in db", ip_entry, ip_entry.counter)
        ip_entry.counter = count
        ip_entry.save()
    else:
        # else add with def val 1
        counter = count
        ip_entry = IpCounter(ip=ip, counter=counter)
        print("not in db", ip_entry, ip_entry.counter)
        ip_entry.save()
