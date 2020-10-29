from django import forms

from applications.homepage.models import Link


class UrlInputForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = [Link.original.field.name]
        labels = {Link.original.field.name: ""}
        widgets = {
            Link.original.field.name: forms.TextInput(
                attrs={"placeholder": "Enter your link..."}
            )
        }

    def clean_original(self):
        original = self.data.get("original")
        if not original or Link.objects.filter(shortcut=original):
            raise forms.ValidationError("Enter a valid URL")
        return original
