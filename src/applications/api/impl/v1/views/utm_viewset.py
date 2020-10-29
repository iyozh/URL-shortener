from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from applications.api.impl.v1.serializers.utm_serializer import UtmSerializer
from applications.homepage.models import Link
from applications.statistics.models import UTM
from project.utils import _get_utm_string
from project.utils.object_utils import update_utm


class UtmViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UtmSerializer
    queryset = UTM.objects.all()
    http_method_names = ["put", "get"]

    def update(self, request, *args, **kwargs):
        redirect_response = super().update(request, *args, **kwargs)

        link_id = request.data["link"]

        utm = UTM.objects.filter(link_id=link_id).first()

        utm_string = _get_utm_string(utm)

        update_utm(utm_string, link_id)

        return redirect_response
