from django import forms

from applications.homepage.models import Link


class CheckboxForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["confirm"]
        labels = {"confirm": ""}
