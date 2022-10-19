from django.db import models

from src_django.api.models.person import Person
from src_django.api.models.portfolio import Portfolio


class PersonPortfolio(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
