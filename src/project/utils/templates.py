from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment


def build_jinja2_env(**options):
    env = Environment(**options)
    env.globals.update(
        {
            "static": static,
            "url": reverse,
        }
    )
    return env
