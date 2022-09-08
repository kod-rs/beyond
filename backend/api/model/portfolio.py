from django.db import models

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
    username = models.CharField(max_length=200,unique=False)
    name = models.CharField(max_length=200,unique=False)
    colour_tmp = models.CharField(max_length=200)
