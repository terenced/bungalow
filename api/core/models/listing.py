import uuid

from django.db import models
from localflavor.us.models import USStateField, USZipCodeField

from .common import TimeStampedModel, UUIDModel

AREA_UNITS = [("SqFt", "Square Feet"), ("Mt", "Metric")]

HOME_TYPES = [
    ("Apartment", "Apartment"),
    ("Condominium", "Condominium"),
    ("Duplex", "Duplex"),
    ("MultiFamily2To4", "Multi Family (2 To 4)"),
    ("SingleFamily", "Single Family"),
    ("VacantResidentialLand", "Vacant Residential Land"),
]


class Listing(UUIDModel, TimeStampedModel, models.Model):
    bedrooms = models.IntegerField(default=0)

    # This is a Decimal to account for half bathrooms
    bathrooms = models.DecimalField(max_digits=4, default=0.0, decimal_places=1)

    area_unit = models.CharField(max_length=10, choices=AREA_UNITS, default="SqFt")

    home_size = models.IntegerField(blank=True)

    home_type = models.CharField(
        max_length=100, choices=HOME_TYPES, default="SingleFamily"
    )
    property_size = models.IntegerField(blank=True)

    price = models.DecimalField(max_digits=20, default=0.0, decimal_places=2)

    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = USStateField()
    zipcode = USZipCodeField()

    year_built = models.IntegerField()

    class Meta:
        verbose_name_plural = "Listings"
        unique_together = [["address", "city", "state", "zipcode"]]

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}, {self.zipcode}"
