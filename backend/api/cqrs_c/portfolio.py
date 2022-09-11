from backend.api.model.portfolio import Portfolio


def create_portfolio(username, portfolio_name, colour):
    print(username, portfolio_name, colour)
    i = Portfolio.objects.create(
        username=username,
        name=portfolio_name,
        colour=colour
    )
    i.save()
    return bool(i)


def update_portfolio(username, current_name, params):
    params = {k: v for k, v in params.items() if k in ["name", "colour"]}

    return bool(
        Portfolio.objects \
            .filter(username=username, name=current_name) \
            .update(**params)
    )


def delete_portfolio(username, portfolio_name):
    return bool(
        Portfolio.objects.filter(username=username,
                                 name=portfolio_name).delete()
    )
