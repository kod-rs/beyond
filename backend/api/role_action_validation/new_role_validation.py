
def t(role, path, method):
    print(role, path, method)

    config = {
        "aggregator": {
            "/locations/<int>": {
                "method1": True,
                "method2": False
            }
        },
        "role2": {
            "action1": False,
        }
    }

    if role not in config:
        return False

    paths = config[role]
    if path not in paths:
        return False

    methods = paths[path]

    if method not in methods:
        return False

    return methods[method]


def check(role, path, method):
    return any(t(i, path, method) for i in role)

#
# def main():
#     print(check("role1", "action1"))
#     print(check("role1", "action2"))
#     print(check("role2", "action1"))
#     print(check("role2", "action2"))
#     print(check("role3", "action1"))
#     print(check("role3", "action2"))
#
# if __name__ == '__main__':
#     main()