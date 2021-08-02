from django.views.generic import TemplateView
from rest_framework.authtoken.models import Token


class ApiGuideView(TemplateView):
    template_name = "api_guide/api_guide.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            api_token = Token.objects.filter(user=self.request.user).first()
            ctx.update({"api_token": api_token})
        return ctx
