from django.urls import include, path

v1_patterns = [
    # path("users/", include("api_users.urls")),
    # path("hospitals/", include("api_hospital.urls")),
    # path("blood-donation/", include("api_blood_donation.urls")),
    path("news/", include("api_news.urls")),
]

urlpatterns = [
    path("v1/", include(v1_patterns)),
]
