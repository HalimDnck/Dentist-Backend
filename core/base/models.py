from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    is_archive = models.BooleanField(default=False)
    # DATES
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    archived_at = models.DateTimeField(default=None, null=True)
    # TRANSACTORS
    created_by = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    updated_by = models.ForeignKey('user.User', on_delete=models.CASCADE,null=True)
    archived_by = models.ForeignKey('user.User', on_delete=models.CASCADE,null=True)

    class Meta:
        abstract = True


class DefaultBaseModel(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)

    
    class Meta:
        abstract = True
