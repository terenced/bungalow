import uuid
from django.db import models


class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    """Abstract Model with `id` as a UUID field."""

    id = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4
    )

    class Meta:
        abstract = True
