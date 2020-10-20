import secrets

from django.urls import reverse_lazy
from django.views.generic import FormView

from applications.homepage.forms import UrlInputForm
from applications.homepage.models import Link


class HomePageView(FormView):
    template_name = "homepage/homepage.html"
    form_class = UrlInputForm
    success_url = reverse_lazy("homepage:index")

    def get_initial(self):
        return {Link.original.field.name: self.request.session.get("shortcut")}

    def form_valid(self, form):
        original = form.cleaned_data["original"]
        shortcut = self.request.headers["Referer"] + secrets.token_urlsafe(3)
        user = self.request.user.id
        self.request.session["shortcut"] = shortcut
        url = Link(original=original, shortcut=shortcut, user_id=user)
        url.save()
        return super().form_valid(form)
