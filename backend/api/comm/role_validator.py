from backend.api.comm.json_loader import role_validation_cfg


class SchemeValidator:

    def __init__(self):
        self.scheme = role_validation_cfg
        self.serialization_connector = ";"

    def check_action(self, role, action):
        """"""
        print(f"check action {role=} {action=}")
        if isinstance(action, str):
            action = self.deserialize(action)

        if len(action) == 1:
            return False

        # todo add test for this
        if isinstance(role, list):
            return any([self.check_action(r, action) for r in role])

        if role not in self.scheme["roles"]:
            return False

        t = self.scheme["roles"][role]

        table = action[0]
        action = action[1]
        if table not in t:
            return False
        t = t[table]

        if action not in t:
            return False

        t = t[action]

        return t

    def get_all_tables(self):
        r = []
        for role, tables in self.scheme["roles"].items():

            for t, actions in tables.items():
                r.append(t)

        return r

    def deserialize(self, payload):

        splitters = [self.serialization_connector, " "]

        if not any([payload.__contains__(i) for i in splitters]):
            return [payload]

        if self.serialization_connector in payload:
            return [i.strip() for i in
                    payload.split(self.serialization_connector)]

        else:
            return [i.strip() for i in
                    payload.split(" ", 1) if i.strip()]


def main():
    scheme_validator = SchemeValidator()

    for role_k, role_v in {"aggregator": True, "role_false": False}.items():

        for table_k, table_v in {"location ": True,
                                 "table_false": False}.items():

            for action_k, action_v in {"add single": True,
                                       "action false": False}.items():

                for strip_test in ["", " "]:
                    for connector in [";", " "]:

                        action_composite = table_k + connector + strip_test + action_k

                        for deserialize_option in [True, False]:
                            if deserialize_option:
                                action_composite = scheme_validator.deserialize(
                                    action_composite)

                            print(
                                f"pass {role_k:15} {str(action_composite):15}")
                            print(
                                f"{role_v:10} {table_v:15} {action_v:15} {deserialize_option:15}")

                            r = scheme_validator.check_action(role_k,
                                                              action_composite)

                            if role_v and table_v and action_v:
                                print(f"expecting true, got {r}")
                                if not r:
                                    raise Exception("err")
                            else:
                                print(f"expecting false, got {r}")
                                if r:
                                    raise Exception("err")
                            print()
    print("test ok")


if __name__ == '__main__':
    main()
