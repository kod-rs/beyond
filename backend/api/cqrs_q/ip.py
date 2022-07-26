from backend.api.model.ip import IpCounter


def check_max_count(ip, max_count):
    try:
        ip_obj = IpCounter.objects.get(ip=ip)
        return ip_obj.counter > max_count

    except IpCounter.DoesNotExist:
        return False

