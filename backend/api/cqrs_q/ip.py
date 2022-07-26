from backend.api.model.ip import IpCounter


def check_max_count(ip, max_brute_force_count):
    if IpCounter.objects.filter(ip=ip):
        ip_obj = IpCounter.objects.get(ip=ip)
        print("current count", ip_obj.counter)
        return ip_obj.counter > max_brute_force_count
