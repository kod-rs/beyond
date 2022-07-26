import pathlib

from .keycloak.pem import generate_keys
# from .keycloak.keys_manager import create_tables
from .assets.printer import print_logo

# from django.apps import AppConfig
# class MyAppConfig(AppConfig):
#     name = 'beyond-api'
#     verbose_name = "beyond api"
#     def ready(self):
#         print("startup code")
#         pass # startup code here


def run_startup():

    print_logo()
    # print("setting up")
    # create_tables()
    # print(" 1 key table created")
    # generate_keys()
    # print(" 2 keycloak keys generated")

def main():
    run_startup()


if __name__ == '__main__':
    main()