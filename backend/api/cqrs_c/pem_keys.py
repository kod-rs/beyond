from backend.api.model.pem_keys import PemKeys


def add_keys(key_type, key):

    if isinstance(key, bytes):
        encoding = 'utf-8'
        key = key.decode(encoding)

    k, created = PemKeys.objects.update_or_create(
            key_type=key_type, defaults={"key_value": key}
    )
    k.save()


def remove_key(key_type):
    instance = PemKeys.objects.get(key_type=key_type)
    instance.delete()
