from django.urls import path

from applications.statistics.apps import StatisticsConfig
from applications.statistics.views import LinksView, StatisticsView
from applications.statistics.views.confirm_update import ConfirmUpdateView
from applications.statistics.views.delete import DeleteLinkView
from applications.statistics.views.utm_update import UtmUpdateView

app_name = StatisticsConfig.label


urlpatterns = [
    path("", LinksView.as_view(), name="links"),
    path("<str:pk>/", StatisticsView.as_view(), name="hits"),
    path("<str:pk>/update-confirm", ConfirmUpdateView.as_view(), name="update-confirm"),
    path("<str:pk>/update_utm/", UtmUpdateView.as_view(), name="update_utm"),
    path("<str:pk>/delete/", DeleteLinkView.as_view(), name="delete"),
]
