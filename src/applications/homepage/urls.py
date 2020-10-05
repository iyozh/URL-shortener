from django.urls import path

from applications.homepage.apps import HomepageConfig
from applications.homepage.views import HomePageView

app_name = HomepageConfig.label

urlpatterns = [path("", HomePageView.as_view(), name="index")]
