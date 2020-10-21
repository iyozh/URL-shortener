from django.urls import path

from applications.statistics.apps import StatisticsConfig
from applications.statistics.views import LinksView, StatisticsView
from applications.statistics.views.confirm_update import ConfirmUpdate

app_name = StatisticsConfig.label


urlpatterns = [
    path("", LinksView.as_view(), name="links"),
    path("<str:pk>/", StatisticsView.as_view(), name="hits"),
    path("<str:pk>/update-confirm", ConfirmUpdate.as_view(), name="update-confirm"),
]
