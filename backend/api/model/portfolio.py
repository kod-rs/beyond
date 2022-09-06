from django.db import models
from django.db.models import UniqueConstraint

from backend.api.model.colour import Colour

'''
modify constraints

sudo su postgres
psql

\c beyond
\d api_portfolio
\
alter table api_portfolio drop constraint api_portfolio_pkey CASCADE;
alter table api_portfolio add constraint table_pkey primary key (username, name);

'''


class Portfolio(models.Model):

    # UniqueConstraint(fields=['username', 'name'], name='constraint_name')

    username = models.CharField(max_length=200,unique=False)
    name = models.CharField(max_length=200,unique=False)
    # colour = models.ForeignKey(Colour, on_delete=models.CASCADE)
    colour = models.CharField(max_length=200)

    # class Meta:
    #     # managed = True
    #     db_table="portfolio"
    #     unique_together = (('username',
    #                         'name'),)
