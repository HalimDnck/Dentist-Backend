from django.db import models
from core.base.models import BaseModel


class Gender(BaseModel):
    name = models.CharField(max_length=128, unique=True)
    key = models.CharField(max_length=128, unique=True)


class InsuranceProvider(BaseModel):
    name = models.CharField(max_length=128, unique=True)
    key = models.CharField(max_length=128, unique=True)


class ReferralSource(BaseModel):
    name = models.CharField(max_length=128, unique=True)
    key = models.CharField(max_length=128, unique=True)


class Allergy(BaseModel):
    name = models.CharField(max_length=128, unique=True)
    key = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=600, null=True, blank=True)
