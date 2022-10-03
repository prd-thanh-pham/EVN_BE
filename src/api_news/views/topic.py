from rest_framework import viewsets
from api_news.models import Topic
from api_news.serializers import TopicSerializer


class TopicModelViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
