from django.db import models
from .common import TimeStampedModel


SOURCE_TYPES = [("zillow", "Zillow"), ("internal", "Internal")]


class Metadata(TimeStampedModel, models.Model):
    """Metadata for a listing. 

    Usually data from an external system, for example Zillow.

    NOTE: Initially, we are only supporting Zillow, but I am trying to 
    future-proof this a bit.
    """

    # External ID is a string because other sources (in the future) might
    # not use integers
    external_id = models.CharField(max_length=200)

    source = models.CharField(max_length=100, choices=SOURCE_TYPES, default="internal")

    external_link = models.URLField()

    class Meta:
        indexes = [models.Index(fields=["external_id"])]
