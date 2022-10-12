from django.db import models
from api.models import TimeStampedModel
from api_news.models import News


class Image(TimeStampedModel):
    title = models.CharField(max_length=255, blank=True)
    src = models.CharField(max_length=255, blank=True)
    news = models.ForeignKey(News, related_name="images", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "evn_image"
