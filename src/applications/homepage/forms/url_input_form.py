from django import forms

from applications.homepage.models import Url


class UrlInputForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = [Url.original.field.name]
        labels = {Url.original.field.name: ""}
