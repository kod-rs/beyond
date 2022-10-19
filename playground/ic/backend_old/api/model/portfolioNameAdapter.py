from django.db import models

from playground.ic.backend_old.api.model.nameHistory import NameHistory


class PortfolioColourAdapter(models.Model):
    # alternative primary key
    portfolio = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)

    # foreign key
    history_name_id = models.ForeignKey(
        NameHistory,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    # value
    timestamp_colour_change = models.DateTimeField(auto_now_add=True)
