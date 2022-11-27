from rest_framework.routers import SimpleRouter
from api_news.views import NewsModelViewSet, TopicModelViewSet

app_name = "api_news"

router = SimpleRouter(trailing_slash=False)
router.register(r"news", NewsModelViewSet, basename="news")
router.register(r"topic", TopicModelViewSet, basename="topic")

urlpatterns = router.urls

