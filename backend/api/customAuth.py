from django.contrib.auth.backends import BaseBackend

from .models import User

class ModelBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        # Check the username/password and return a user.
        # ...

        if not request:
            return None

        print("custom auth", username, password)

        print(f"{User.objects=}")
        for i in User.objects.all():
            if i.username == username:
                print("-------------------------------")
            print(i.username, i.id)

        print(20 * " -")

        try:
            user = User.objects.all().get(username=username)
            # print(f"{User.objects=}")
            # print(user)
            print(80 * "-")
            print("found user")
            print(user)

            return user

        except User.DoesNotExist:
            return None

        # # return User()
        #
        # # return True
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


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None