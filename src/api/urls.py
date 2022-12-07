from django.urls import include, path

v1_patterns = [
    path("", include("api_news.urls")),
]

urlpatterns = [
    path("v1/", include(v1_patterns)),
]
