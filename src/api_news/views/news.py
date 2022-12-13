from rest_framework import viewsets, status
from rest_framework.decorators import action
from api_news.services import CrawlService
from api_news.models import News
from api_news.serializers import NewsSerializer
from rest_framework.response import Response


class NewsModelViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @action(methods=["get"], detail=False)
    def crawl(self, request, *args, **kwargs):
        CrawlService.thread_crawl.after_response()
        print("Crawl finished")
        return Response(
            {"success": "Method crawl data is in progress"}, status=status.HTTP_200_OK
        )
