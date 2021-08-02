from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from applications.homepage.models import Link


class LinksView(LoginRequiredMixin, ListView):
    template_name = "statistics/links.html"
    model = Link
    paginate_by = 8

    def get_queryset(self):
        queryset = Link.objects.filter(user_id=self.request.user.id)
        return queryset
