from rest_framework import viewsets
from api_news.models import Image
from api_news.serializers import ImageSerializer


class ImageModelViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
