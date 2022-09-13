from django.db import models

from backend.api.model.colourHistory import ColourHistory
from backend.api.model.portfolio import Portfolio


class PortfolioColourAdapter(models.Model):
    # alternative primary key
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    # portfolio = models.CharField(max_length=200, blank=True, null=True)
    # username = models.CharField(max_length=200, blank=True, null=True)

    # foreign key
    colour = models.ForeignKey(
        ColourHistory,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    # value
    timestamp = models.DateTimeField(auto_now_add=True)
