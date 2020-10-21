from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from applications.homepage.models import Link
from applications.statistics.forms.checkbox import CheckboxForm
from applications.statistics.models import Hit


class StatisticsView(FormMixin, DetailView):
    template_name = "statistics/statistics.html"
    model = Link
    form_class = CheckboxForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        hits = Hit.objects.filter(url_id=self.object.id)

        ctx.update({"hits": hits})
        return ctx

    def get_initial(self):
        return {Link.confirm.field.name: self.object.confirm}
