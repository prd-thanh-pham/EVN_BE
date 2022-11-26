import uuid

from django.db import models
from api.models import TimeStampedModel
from api_news.models import News


class Image(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(max_length=255, blank=True)
    src = models.CharField(max_length=255, blank=True)
    news = models.ForeignKey(
        News, related_name="images", on_delete=models.CASCADE, null=True, blank=True
    )
    order = models.IntegerField(default=0)

    class Meta:
        db_table = "evn_image"
