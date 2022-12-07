from rest_framework import serializers
from api_news.models import Topic
from api_news.serializers import NewsSerializer


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class TopicDetailSerializer(serializers.ModelSerializer):
    news = NewsSerializer(many=True, required=False)

    class Meta:
        model = Topic
        fields = [
            "id",
            "name",
            "source",
            "news",
        ]
