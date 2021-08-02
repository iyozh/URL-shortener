from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("applications.homepage.urls")),
    path("onboarding/", include("applications.onboarding.urls")),
    path("statistics/", include("applications.statistics.urls")),
    path("guide/", include("applications.api_guide.urls")),
    path("api/", include("applications.api.urls")),
    path("", include("social_django.urls")),
]
