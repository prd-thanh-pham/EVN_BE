from rest_framework import viewsets
from api_news.models import Source
from api_news.serializers import SourceSerializer


class SourceModelViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
