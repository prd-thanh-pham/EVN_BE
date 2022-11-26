from rest_framework import serializers
from api_news.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["title", "src", "order"]
