from django.db import models
from .common import TimeStampedModel
from .listing import Listing

SOURCE_TYPES = [("zillow", "Zillow"), ("internal", "Internal")]


class Metadata(TimeStampedModel, models.Model):
    """Metadata for a listing. 

    Usually data from an external system, for example Zillow.

    NOTE: Initially, we are only supporting Zillow, but I am trying to 
    future-proof this a bit.
    """

    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    # External ID is a string because other sources (in the future) might
    # not use integers
    external_id = models.CharField(max_length=200)
    external_link = models.URLField()
    source = models.CharField(max_length=100, choices=SOURCE_TYPES, default="internal")

    rent_price = models.DecimalField(
        max_digits=20, default=0.0, decimal_places=2, blank=True, null=True
    )

    # rentzestimate_amount
    estimated_rent = models.DecimalField(
        max_digits=20, default=0.0, decimal_places=2, blank=True, null=True
    )
    # rentzestimate_last_updated
    estimated_rent_updated = models.DateField(blank=True, null=True)

    tax_value = models.DecimalField(
        max_digits=20, default=0.0, decimal_places=2, blank=True, null=True
    )
    tax_year = models.IntegerField(blank=True, null=True)

    # zestimate_amount
    estimated_sale_price = models.DecimalField(
        max_digits=20, default=0.0, decimal_places=2, blank=True, null=True
    )
    # zestimate_last_updated
    estimated_sale_price_updated = models.DateField(blank=True, null=True)

    class Meta:
        indexes = [models.Index(fields=["external_id"])]
