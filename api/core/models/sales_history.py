from django.db import models

from .common import TimeStampedModel
from .listing import Listing


class SalesHistory(TimeStampedModel, models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    sold_date = models.DateField()
    sold_price = models.DecimalField(max_digits=20, default=0.0, decimal_places=2)
