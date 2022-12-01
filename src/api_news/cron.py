import datetime
import logging

logger = logging.getLogger(__name__)
from django.db import transaction
from api_news.models import News, Topic
from api_news.services import CrawlService, NewsService


def crawl_every_day():
    print("thanh")
    t = Topic.objects.create(name="thanh123")
    t.save()
    # print("\n\nHello World....!! ", timezone.now())\
    s = "\nHello World....!! " + str(datetime.datetime.now())
    with open("news.txt", "a") as file:
        file.write(s)

    # data = CrawlService.crawl('https://www.evn.com.vn/')
    # with transaction.atomic():
    #     news_data = NewsService.create_list_news(data)
    #     news_objs = News.objects.bulk_create(news_data, ignore_conflicts=True)
    #     image_data = ImageService.create_list_image(data, news_objs)
    #     Image.objects.bulk_create(image_data, ignore_conflicts=True)

    # print(2)
