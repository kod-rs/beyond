from backend.api.model.pem_keys import PemKeys


def add_jwt_public_key(key_type, key):
    """
    add or update key

    """

    if isinstance(key, bytes):
        encoding = 'utf-8'
        key = key.decode(encoding)

    k, _ = PemKeys.objects.update_or_create(
        key_type=key_type, defaults={"key_value": key}
    )
    k.save()


def remove_jwt_public_key(key_type):
    instance = PemKeys.objects.get(key_type=key_type)
    instance.delete()
