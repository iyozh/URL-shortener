import datetime
from typing import Dict

from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError
from httpagentparser import simple_detect


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def get_hit_params(request) -> Dict:
    ip = get_client_ip(request)
    time = datetime.datetime.now()
    try:
        location = GeoIP2().country_name(ip)

    except AddressNotFoundError:
        location = "Undefined"

    params = {"ip_address": ip, "time": time, "location": location}

    user_agent = simple_detect(request.META["HTTP_USER_AGENT"])

    for key, value in zip(("os", "browser"), user_agent):
        params.setdefault(key, value)

    return params
