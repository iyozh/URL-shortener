from django.views.generic import DetailView

from applications.homepage.models import Link
from applications.statistics.models import Hit


class StatisticsView(DetailView):
    template_name = "statistics/statistics.html"
    model = Link

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        hits = Hit.objects.filter(url_id=self.object.id)

        ctx.update({"hits":hits})
        return ctx