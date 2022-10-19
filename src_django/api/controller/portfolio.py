import typing

from django.forms.models import model_to_dict

from src_django.api.models import PersonPortfolio


def get_user_portfolios(user_id: str
                        ) -> typing.Union[typing.List[dict], None]:
    filter_res = PersonPortfolio.objects.filter(person__id=user_id)
    filter_res = list(filter_res)
    if not filter_res:
        return
    person_portfolios = [model_to_dict(p.portfolio) for p in filter_res]
    return person_portfolios
