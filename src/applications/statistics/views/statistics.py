from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from applications.homepage.models import Link
from applications.statistics.forms.checkbox import CheckboxForm
from applications.statistics.forms.utm_form import UtmForm
from applications.statistics.models import Hit
from project.utils.object_utils import _get_utm_initial_values


class StatisticsView(FormMixin, DetailView):
    template_name = "statistics/statistics.html"
    model = Link
    form_class = CheckboxForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        hits = Hit.objects.filter(link_id=self.object.id)
        initial_values = _get_utm_initial_values(self.object)
        utm = UtmForm(initial=initial_values)
        ctx.update({"hits": hits, "utm": utm})
        return ctx

    def get_initial(self):
        return {Link.confirm.field.name: self.object.confirm}
