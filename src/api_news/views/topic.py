from rest_framework import viewsets, status
from rest_framework.response import Response

from api_news.models import Topic
from api_news.serializers import TopicSerializer
from api_news.serializers.topic import TopicDetailSerializer


class TopicModelViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def retrieve(self, request, pk=None):
        if pk:
            queryset = Topic.objects.filter(id=pk)
        serializer = TopicDetailSerializer(queryset[0], many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
