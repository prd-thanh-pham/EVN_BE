from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.decorators import action
from api_news.services import CrawlService, NewsService, ImageService
from api_news.models import News, Image
from api_news.serializers import NewsSerializer
from rest_framework.response import Response


class NewsModelViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @action(methods=["get"], detail=False)
    def crawl(self, request, *args, **kwargs):
        data = CrawlService.crawl('https://www.evn.com.vn/')
        try:
            with transaction.atomic():
                news_data = NewsService.create_list_news(data)
                news_objs = News.objects.bulk_create(news_data)
                image_data = ImageService.create_list_image(data, news_objs)
                Image.objects.bulk_create(image_data)
            return Response(
                {"success": "Crawl data is success"},
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response({"error_msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)
