import uuid
from django.db import models
from api.models.timestamped import TimeStampedModel
from api_news.models import Topic


class News(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    title = models.CharField(max_length=255, blank=True)
    post_at = models.CharField(max_length=255, blank=True)
    thumbnail = models.CharField(max_length=255, blank=True)
    topic = models.ForeignKey(
        Topic, related_name="news", on_delete=models.SET_NULL, null=True, blank=True
    )
    source = models.CharField(max_length=255, blank=True, unique=True)
    author = models.CharField(max_length=255, blank=True)
    excerpt = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "evn_news"
        ordering = ["-post_at"]
