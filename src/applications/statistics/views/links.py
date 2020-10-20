from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from applications.homepage.models import Url


class LinksView(LoginRequiredMixin, ListView):
    template_name = "statistics/links.html"
    model = Url
