import secrets

from django import forms
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView

from applications.homepage.models import Url


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
        self.request.session["shortcut"] = shortcut
        url = Url(original=original, shortcut=shortcut)
        url.save()
        return super().form_valid(form)


class RedirectToOriginalView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        absolute_url = self.request.build_absolute_uri()
        url = Url.objects.get(shortcut=absolute_url)
        return url.original
