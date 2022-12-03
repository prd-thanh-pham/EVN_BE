from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.decorators import action
from api_news.services import (
    CrawlService,
    NewsService,
    ContentService,
    KeywordService,
)
from api_news.models import News, Topic, Content, Keyword
from api_news.serializers import NewsSerializer
from rest_framework.response import Response


class NewsModelViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @action(methods=["get"], detail=False)
    def crawl(self, request, *args, **kwargs):
        list_topic = Topic.objects.all()
        for topic in list_topic:
            data = CrawlService.crawl_from_url(topic.source)
            try:
                with transaction.atomic():
                    data, news_data = NewsService.create_list_news(data, topic)
                    news_objs = News.objects.bulk_create(
                        news_data, ignore_conflicts=True
                    )
                    content_data = ContentService.create_list_content(data, news_objs)
                    keyword_data = KeywordService.create_list_keyword(data, news_objs)
                    Content.objects.bulk_create(content_data, ignore_conflicts=True)
                    Keyword.objects.bulk_create(keyword_data, ignore_conflicts=True)
            except Exception as e:
                return Response(
                    {"error_msg": str(e)}, status=status.HTTP_400_BAD_REQUEST
                )
        return Response(
            {"success": "Crawl data is success"}, status=status.HTTP_200_OK
        )
