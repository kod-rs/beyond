from backend_old.api.model_security.csrf import CSRF


def get_by_ip(ip):
    if CSRF.objects.filter(ip=ip).exists():
        entry = CSRF.objects.get(ip=ip)

        return entry

    return None
