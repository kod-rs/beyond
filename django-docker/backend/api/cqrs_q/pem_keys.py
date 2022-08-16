from backend.api.model.pem_keys import PemKeys


def get_all_keys():
    return PemKeys.objects.all()
