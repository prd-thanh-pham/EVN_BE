from datetime import datetime
from celery import shared_task
from api_news.models import Topic


@shared_task
def crawl_newsfeed():
    print("thanh")
    t = Topic.objects.create(name="thanh123")
    t.save()
    # print("\n\nHello World....!! ", timezone.now())\
    s = "\nHello World....!! " + str(datetime.datetime.now())
    with open("news.txt", "a") as file:
        file.write(s)
