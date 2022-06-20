from django.contrib.auth.backends import BaseBackend

class ModelBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        # Check the username/password and return a user.
        ...

        print("custom auth")

        return True
        # UserModel = get_user_model()
        # if username is None:
        #     username = kwargs.get(UserModel.USERNAME_FIELD)
        # try:
        #     user = UserModel._default_manager.get_by_natural_key(username)
        #     if user.check_password(password):
        #         return user
        # except UserModel.DoesNotExist:
        #     # Run the default password hasher once to reduce the timing
        #     # difference between an existing and a non-existing user (#20760).
        #     UserModel().set_password(password)