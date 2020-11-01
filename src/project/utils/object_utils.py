from typing import Dict

from applications.homepage.models import Link
from applications.statistics.models import UTM


def _get_utm_initial_values(link_object) -> Dict:
    initial_params = {}
    for field in UTM._meta.get_fields():
        initial_params.setdefault(
            field.attname, getattr(link_object.utm, field.attname, None)
        )
    return initial_params


def _get_utm_string(utm_object):
    utm_string = "?"

    for field in UTM._meta.get_fields():
        if field.attname == "link_id" or not getattr(utm_object, field.attname):
            continue
        utm_string += f"{field.attname}={getattr(utm_object, field.attname)}&"

    return utm_string


def _update_utm(utm_string, link_id):

    link = Link.objects.filter(id=link_id).first()

    new = link.utm_copy + utm_string
    link.original = new
    link.save()

    return link.utm
