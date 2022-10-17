
from backend_old.api.model_security.csrf import CSRF


# get_or_create
# update_or_create

def create(ip, synchronizer_token, encrypted_token, double_submitted_cookie):

    d, _ = CSRF.objects.update_or_create(ip=ip, defaults={
            "synchronizer_token" : synchronizer_token,
             "encrypted_token" : encrypted_token,
           "double_submitted_cookie" : double_submitted_cookie
        }
    )

    d.save()
