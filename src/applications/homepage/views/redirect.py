from django.http import Http404, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import RedirectView

from applications.homepage.models import Link
from applications.statistics.models import Hit
from project.utils.web_utils import get_hit_params


class RedirectToOriginalView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):

        redirect_url = Link.objects.filter(
            shortcut__contains=self.kwargs.get("key")
        ).first()

        if not redirect_url:
            raise Http404

        if redirect_url.confirm:
            if redirect_url.marker:
                redirect_url.marker = False
                redirect_url.save()
                return reverse_lazy(
                    "homepage:confirmation", kwargs={"pk": redirect_url.pk}
                )

        if not redirect_url.marker:
            redirect_url.marker = True
            redirect_url.save()

        params = get_hit_params(self.request)
        hit = Hit(**params, link_id=redirect_url.id)
        hit.save()
        return redirect_url.original
