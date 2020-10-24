from typing import Dict

from applications.statistics.models import UTM


def _get_utm_initial_values(link_object, model=UTM) -> Dict:
    initial_params = {}
    for field in model._meta.get_fields():
        initial_params.setdefault(
            field.attname, getattr(link_object.utm, field.attname, None)
        )
    return initial_params


def _get_utm_string(link_object, model=UTM):
    utm_string = "?"

    for field in model._meta.get_fields():
        if field.attname == "link_id" or getattr(link_object, field.attname) is None:
            continue
        utm_string += f"{field.attname}={getattr(link_object, field.attname)}&"

    return utm_string
