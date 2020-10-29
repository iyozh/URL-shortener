from django.views.generic import TemplateView


class ApiGuideView(TemplateView):
    template_name = "api_guide/api_guide.html"
