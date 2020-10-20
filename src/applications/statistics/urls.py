from django.urls import path

from applications.statistics.apps import StatisticsConfig
from applications.statistics.views import LinksView, StatisticsView

app_name = StatisticsConfig.label


urlpatterns = [
    path("", LinksView.as_view(), name="links"),
    path("<str:pk>/", StatisticsView.as_view(), name="hits"),
]
