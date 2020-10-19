from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from applications.homepage.models import Url


class StatisticView(LoginRequiredMixin, ListView):
    template_name = "statistics/statistics.html"
    model = Url
