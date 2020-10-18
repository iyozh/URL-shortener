from django.views.generic import ListView

from applications.homepage.models import Url


class StatisticView(ListView):
    template_name = "statistics/statistics.html"
    model = Url
