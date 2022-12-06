from rest_framework.routers import SimpleRouter
from api_news.views import NewsModelViewSet, TopicModelViewSet
from api_news.views.search import SearchModelViewSet

app_name = "api_news"

router = SimpleRouter(trailing_slash=False)
router.register(r"news", NewsModelViewSet, basename="news")
router.register(r"topic", TopicModelViewSet, basename="topic")
router.register(r"search", SearchModelViewSet, basename="search")

urlpatterns = router.urls
