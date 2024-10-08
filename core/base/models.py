from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_deleted = models.BooleanField(default=False)
    name = models.CharField(max_length=128, null=True, blank=True)
    slug = models.CharField(max_length=128, null=True, blank=True)
    # DATES
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True)
    # TRANSACTORS
    created_by = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True)
    updated_by = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True)
    deleted_by = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = kwargs.pop("user", None)

        if self.name:
            self.slug = slugify(self.name)

        if self.pk:
            self.updated_at = timezone.now()
            if user:
                self.updated_by = user
        else:
            if user:
                self.created_by = user

        super(BaseModel, self).save(*args, **kwargs)


class DefaultBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
