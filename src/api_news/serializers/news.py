from rest_framework import serializers
from api_news.models import News
from api_news.serializers.content import ContentSerializer
from api_news.serializers.keyword import KeywordSerializer


class NewsSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, required=False)
    keywords = KeywordSerializer(many=True, required=False)

    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "post_at",
            "thumbnail",
            "topic",
            "source",
            "author",
            "excerpt",
            "contents",
            "keywords",
        ]
