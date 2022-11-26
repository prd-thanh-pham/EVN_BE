from rest_framework import serializers
from api_news.models import Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["paragraph", "order"]
