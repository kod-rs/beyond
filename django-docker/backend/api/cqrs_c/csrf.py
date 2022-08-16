from backend.api.model.csrf import CSRF


def create(ip, synchronizer_token, encrypted_token, double_submitted_cookie):
    d, _ = CSRF.objects.update_or_create(
        ip=ip,
        defaults={"synchronizer_token": synchronizer_token,
                  "encrypted_token": encrypted_token,
                  "double_submitted_cookie": double_submitted_cookie})
    d.save()
