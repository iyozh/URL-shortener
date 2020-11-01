from django.views.generic import UpdateView

from applications.statistics.forms.utm_form import UtmForm
from applications.statistics.models import UTM
from project.utils.object_utils import _get_utm_string, _update_utm


class UtmUpdateView(UpdateView):
    model = UTM
    http_method_names = ["post"]
    form_class = UtmForm

    def form_valid(self, form):
        redirect_response = super().form_valid(form)

        utm_string = _get_utm_string(self.object)

        _update_utm(utm_string, self.object.link_id)

        return redirect_response
