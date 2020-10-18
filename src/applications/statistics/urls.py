from django.urls import path

from applications.statistics.apps import StatisticsConfig
from applications.statistics.views import StatisticView

app_name = StatisticsConfig.label


urlpatterns = [path("", StatisticView.as_view(), name="stats")]
