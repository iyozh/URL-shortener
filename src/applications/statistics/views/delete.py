from django.urls import reverse_lazy
from django.views.generic import DeleteView

from applications.homepage.models import Link


class DeleteLinkView(DeleteView):
    model = Link
    http_method_names = ["post"]
    success_url = reverse_lazy("statistics:links")
