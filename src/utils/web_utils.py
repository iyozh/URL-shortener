import datetime

from httpagentparser import detect, simple_detect


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def get_hit_params(request):
    ip = get_client_ip(request)
    time = datetime.datetime.now()
    params = {"ip_adress": ip, "time": time}
    user_agent = simple_detect(request.META["HTTP_USER_AGENT"])

    for key, value in zip(("os", "browser"), user_agent):
        params.setdefault(key, value)

    return params
