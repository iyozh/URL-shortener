from django.views.generic import DetailView

from applications.homepage.models import Link


class ConfirmationView(DetailView):
    template_name = "homepage/confirmation.html"
    model = Link
