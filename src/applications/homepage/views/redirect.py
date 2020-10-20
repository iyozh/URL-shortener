from django.views.generic import RedirectView
from dynaconf import settings as _ds

from applications.homepage.models import Link
from applications.statistics.models import Hit
from project.utils.web_utils import get_hit_params


class RedirectToOriginalView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        absolute_url = self.request.build_absolute_uri()
        params = get_hit_params(self.request)

        if _ds.ACCOUNT_DEFAULT_HTTP_PROTOCOL == "https":
            absolute_url = absolute_url.replace("http:", "https:")

        redirect_url = Link.objects.filter(shortcut=absolute_url).first()
        hit = Hit(**params, url_id=redirect_url.id)
        hit.save()
        return redirect_url.original
