from django import forms

from applications.statistics.models import UTM


class UtmForm(forms.ModelForm):
    class Meta:
        model = UTM
        fields = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content"]
        labels = {
            UTM.utm_source.field.name: "utm_source",
            UTM.utm_medium.field.name: "utm_medium",
            UTM.utm_campaign.field.name: "utm_campaign",
            UTM.utm_term.field.name: "utm_term",
            UTM.utm_content.field.name: "utm_content",
        }
