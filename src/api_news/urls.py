from rest_framework.routers import SimpleRouter
from api_news.views import NewsModelViewSet, TopicModelViewSet, SourceModelViewSet

app_name = "api_news"

router = SimpleRouter(trailing_slash=False)
router.register(r"", NewsModelViewSet, basename="news")
router.register(r"topic", TopicModelViewSet, basename="topic")
router.register(r"source", SourceModelViewSet, basename="source")

urlpatterns = router.urls
