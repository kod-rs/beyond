from django.db import models

from backend.api.model.colourHistory import ColourHistory
from backend.api.model.portfolioNameHistory import PortfolioNameHistory


class PortfolioHistoryAdapter(models.Model):
    # alternative primary key
    portfolio = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)

    # foreign key
    history_colour_id = models.ForeignKey(
        ColourHistory,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    history_name_id = models.ForeignKey(
        PortfolioNameHistory,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    # value
    timestamp_colour_change = models.DateTimeField(auto_now_add=True)
