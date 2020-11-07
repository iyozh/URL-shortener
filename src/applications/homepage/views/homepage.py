import secrets

from django.urls import reverse_lazy
from django.views.generic import FormView

from applications.homepage.forms import UrlInputForm
from applications.homepage.models import Link
from applications.statistics.models import UTM


class HomePageView(FormView):
    template_name = "homepage/homepage.html"
    form_class = UrlInputForm
    success_url = reverse_lazy("homepage:index")

    def get_initial(self):
        initial_link = self.request.session.get("shortcut")
        if initial_link:
            initial_link = initial_link.replace(f"{self.request.scheme}://", "")
        return {
            Link.original.field.name: initial_link
        }

    def form_valid(self, form):
        original = form.cleaned_data["original"]

        shortcut = self.request.headers["Referer"] + secrets.token_urlsafe(3)

        self.request.session["shortcut"] = shortcut
        self.request.session.set_expiry(0)

        url = Link(
            original=original,
            shortcut=shortcut,
            user_id=self.request.user.id,
            utm_copy=original,
        )
        url.save()

        utm = UTM(link_id=url.id)
        utm.save()

        return super().form_valid(form)
