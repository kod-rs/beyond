# from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth.models import User
#
#
# class ModelBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None):
#
#         if not request:
#             return None
#
#         # print(User.objects.)
#         print("custom auth", username, password)
#         try:
#             user = User.objects.get(username=username)
#             print(user.password)
#
#             if user.password == password:
#                 print("------------ password ok")
#
#                 return user
#
#             else:
#                 print("------------ password mismatch")
#                 return None
#
#         except User.DoesNotExist:
#             print("------------------not found")
#             return None
#
#         # # return User()
#         #
#         # # return True
#         # UserModel = get_user_model()
#         # if username is None:
#         #     username = kwargs.get(UserModel.USERNAME_FIELD)
#         # try:
#         #     user = UserModel._default_manager.get_by_natural_key(username)
#         #     if user.check_password(password):
#         #         return user
#         # except UserModel.DoesNotExist:
#         #     # Run the default password hasher once to reduce the timing
#         #     # difference between an existing and a non-existing user (#20760).
#         #     UserModel().set_password(password)
#
#
#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None