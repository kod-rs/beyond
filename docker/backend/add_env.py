import sys
from pathlib import Path


def fix_settings():
    settings_path = (Path(__file__).resolve().parent
                     / 'src_django'
                     / 'settings'
                     / 'dev.py')

    with open(settings_path, 'r') as file:
        data = file.readlines()

    data = list(map(lambda x: x.replace(
        'from decouple import config\n',
        'from decouple import Config, RepositoryEnv\n'),
                    data))

    index = data.index('from decouple import Config, RepositoryEnv\n')

    env_file_path = str(Path(__file__).resolve().parent / '.env')
    data.insert(index + 1, f'DOTENV_FILE = "{env_file_path}"\n')
    data.insert(index + 2, 'config = Config(RepositoryEnv(DOTENV_FILE))\n')

    with open(settings_path, 'w') as file:
        file.writelines(data)


def fix_env():
    env_file_path = str(Path(__file__).resolve().parent / '.env')
    with open(env_file_path, 'r') as file:
        data = file.readlines()

    data = list(map(lambda x: x.replace(
        'KEYCLOAK_URL=http://localhost:8080/\n',
        'KEYCLOAK_URL=http://0.0.0.0:8080/\n'), data))

    new_data = []
    for line in data:
        if str(line).startswith('BEYOND_PUBLIC_KEY_PATH'):
            line = 'BEYOND_PUBLIC_KEY_PATH = ./beyond_keys/pub.key\n'
        elif str(line).startswith('FLEXOPT_PRIVATE_KEY_PATH'):
            line = 'FLEXOPT_PRIVATE_KEY_PATH = ./flexopt_keys/priv.key\n'
        elif str(line).startswith('FLEXOPT_PUBLIC_KEY_PATH'):
            line = 'FLEXOPT_PUBLIC_KEY_PATH = ./flexopt_keys/pub.key\n'
        new_data.append(line)

    with open(env_file_path, 'w') as file:
        file.writelines(new_data)


def main():
    fix_env()
    fix_settings()


if __name__ == '__main__':
    sys.exit(main())
