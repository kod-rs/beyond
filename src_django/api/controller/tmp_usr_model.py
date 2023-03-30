from src_django.api.models import TempUserModel


def add(user_token, username, user_id) -> bool:
    try:
        new_temp_usr_model = TempUserModel(user_token=user_token,
                                        username=username,
                                        user_id=user_id)
        new_temp_usr_model.save()
    except Exception as e:
        print(f'error={e}')
        return False
    return True

def get_by_user_id(user_id):
    try:
        query_res = TempUserModel.objects.get(user_id=user_id)
        return query_res.username
    except Exception as e:
        print(f'error={e}')
        return False
