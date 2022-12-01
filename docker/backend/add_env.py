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

    with open(env_file_path, 'w') as file:
        file.writelines(data)


def main():
    fix_env()
    fix_settings()


if __name__ == '__main__':
    sys.exit(main())
