from django.views.generic import DetailView

from applications.homepage.models import Url


class StatisticsView(DetailView):
    template_name = "statistics/statistics.html"
    model = Url
