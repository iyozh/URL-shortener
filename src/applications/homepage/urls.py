from django.urls import path, re_path

from applications.homepage.apps import HomepageConfig
from applications.homepage.views import HomePageView, RedirectToOriginalView

app_name = HomepageConfig.label

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    re_path("(?P<key>.{4})$", RedirectToOriginalView.as_view(), name="redirect"),
]
