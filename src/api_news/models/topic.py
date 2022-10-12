import uuid
from django.db import models
from api.models.timestamped import TimeStampedModel


class Topic(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = "evn_topic"
        ordering = ["-created_at"]
