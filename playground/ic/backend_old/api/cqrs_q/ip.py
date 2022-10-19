from playground.ic.backend_old.api.model_security.ip import IpCounter


def check_max_count(ip, max_count):
    try:

        ip_obj = IpCounter.objects.get(ip=ip)
        # print(ip_obj, ip_obj.counter)
        return ip_obj.counter > max_count

    except IpCounter.DoesNotExist:
        return False
