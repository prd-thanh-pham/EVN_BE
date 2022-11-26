import uuid

from django.db import models
from api_news.models import News


class Content(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    paragraph = models.TextField(blank=True)
    news = models.ForeignKey(
        News, related_name="contents", on_delete=models.CASCADE, null=True, blank=True
    )
    order = models.IntegerField(default=0)

    class Meta:
        db_table = "evn_content"
