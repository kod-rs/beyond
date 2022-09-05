from backend.api.model.portfolio import Portfolio


def create_or_update(username, current_name, new_name, colour):

    print("create_or_update")

    print(f"if have {username=} {current_name=}")
    print(f"update this {new_name=} {colour=}")
    i, _ = Portfolio.objects.update_or_create(
        username=username, name=current_name,
        defaults={"name": new_name, "colour": colour}
    )
    print(i)
    i.save()
