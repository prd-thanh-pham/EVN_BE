import uuid
from django.db import models
from api.models.timestamped import TimeStampedModel


class Source(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False, unique=True)
    domain = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)


class Meta:
    db_table = "evn_source"
    ordering = ["-created_at"]
