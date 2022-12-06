from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from api_news.models import News
from api_news.serializers import NewsSerializer


class SearchModelViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
        "title",
        "excerpt",
    ]
    search_fields = [
        "title",
        "excerpt",
    ]
