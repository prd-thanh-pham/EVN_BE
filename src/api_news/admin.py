from django.contrib import admin

from api_news.models import Topic, News

# Register your models here.
admin.site.register(Topic)
admin.site.register(News)
