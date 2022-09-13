from django.db import models

from backend.api.model.colourHistory import ColourHistory
from backend.api.model.portfolio import Portfolio


class PortfolioColourAdapter(models.Model):
    # alternative primary key
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    colour = models.ForeignKey(
        ColourHistory,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    # value
    timestamp = models.DateTimeField(auto_now_add=True)
