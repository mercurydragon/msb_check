from django.db import models

from model_utils.models import TimeStampedModel


class Check(TimeStampedModel):
    tin = models.CharField(max_length=12, blank=True)
    prsn = models.CharField(max_length=15, blank=True)
    result = models.NullBooleanField()
