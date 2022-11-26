import uuid

from django.db import models
from api.models import TimeStampedModel
from api_news.models import News


class Keyword(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    keyword = models.CharField(max_length=255, blank=True)
    news = models.ForeignKey(
        News, related_name="keywords", on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        db_table = "evn_keyword"
