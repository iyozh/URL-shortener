from django.urls import path

from applications.api_guide.apps import ApiGuideConfig
from applications.api_guide.views.api_guide import ApiGuideView

app_name = ApiGuideConfig.label

urlpatterns = [path("", ApiGuideView.as_view(), name="index")]
