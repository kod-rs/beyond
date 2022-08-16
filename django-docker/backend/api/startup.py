from backend.api.assets.printer import print_logo


def run_startup():
    print_logo()


def main():
    run_startup()


if __name__ == '__main__':
    main()
