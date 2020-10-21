from django.views.generic import UpdateView

from applications.homepage.models import Link
from applications.statistics.forms.checkbox import CheckboxForm


class ConfirmUpdate(UpdateView):
    model = Link
    http_method_names = ["post"]
    form_class = CheckboxForm
