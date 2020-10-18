import secrets

from django import forms
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView
from dynaconf import settings as _ds

from applications.homepage.models import Url
from applications.statistics.models import Hit
from utils.web_utils import get_client_ip


class UrlInputForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = [Url.original.field.name]
        labels = {Url.original.field.name: ""}


class HomePageView(FormView):
    template_name = "homepage/homepage.html"
    form_class = UrlInputForm
    success_url = reverse_lazy("homepage:index")

    def get_initial(self):
        return {Url.original.field.name: self.request.session.get("shortcut")}

    def form_valid(self, form):
        original = form.cleaned_data["original"]
        shortcut = self.request.headers["Referer"] + secrets.token_urlsafe(3)
        user = self.request.user.id
        self.request.session["shortcut"] = shortcut
        url = Url(original=original, shortcut=shortcut, user_id=user)
        url.save()
        return super().form_valid(form)


class RedirectToOriginalView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        absolute_url = self.request.build_absolute_uri()
        ip = get_client_ip(self.request)
        browser = self.request.META["HTTP_USER_AGENT"]

        # if _ds.ACCOUNT_DEFAULT_HTTP_PROTOCOL == "https":
        #     absolute_url = absolute_url.replace("http:", "https:")
        redirect_url = Url.objects.filter(shortcut=absolute_url).first()
        hit = Hit(ip_adress=ip, browser=browser, url_id=redirect_url.id)
        hit.save()
        return redirect_url.original
