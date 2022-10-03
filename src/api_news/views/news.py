from rest_framework import viewsets
from api_news.models import News
from api_news.serializers import NewsSerializer


class NewsModelViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
