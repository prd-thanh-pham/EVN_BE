from rest_framework import viewsets
from api_news.models import Topic, News
from api_news.serializers import TopicSerializer
from api_news.serializers.topic import TopicDetailSerializer


class TopicModelViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def retrieve(self, request, pk=None):
        if pk:
            queryset = Topic.objects.filter(id=pk)
        serializer = TopicDetailSerializer(queryset, many=True)
        return self.get_paginated_response(self.paginate_queryset(serializer.data))
