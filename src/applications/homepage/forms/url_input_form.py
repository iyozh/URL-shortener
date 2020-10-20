from django import forms

from applications.homepage.models import Link


class UrlInputForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = [Link.original.field.name]
        labels = {Link.original.field.name: ""}
