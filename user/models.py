from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def name(self):
        return self.first_name + " " + self.last_name
