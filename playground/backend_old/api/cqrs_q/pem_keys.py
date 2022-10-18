from playground.backend_old.api.model_security.pem_keys import PemKeys


def get_all_keys():
    return PemKeys.objects.all()
