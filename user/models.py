# auth/models.py

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class User(AbstractUser):
    id = models.BigIntegerField(primary_key=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

