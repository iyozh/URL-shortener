from django.db.models import Q
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from applications.api.impl.v1.serializers import LinkSerializer
from applications.api.impl.v1.serializers.utm_serializer import UtmSerializer
from applications.homepage.models import Link
from applications.statistics.models import UTM
from project.utils import _get_utm_string
from project.utils.object_utils import update_utm


class UtmViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UtmSerializer
    queryset = UTM.objects.all()
    http_method_names = ["patch", "get"]

    def update(self, request, *args, **kwargs):
        redirect_response = super().update(request, *args, **kwargs)

        link_id = kwargs["pk"]

        utm = UTM.objects.filter(link_id=link_id).first()

        utm_string = _get_utm_string(utm)

        update_utm(utm_string, link_id)

        return redirect_response

    def retrieve(self, request, *args, **kwargs):
        instance = Link.objects.filter(Q(user_id=self.request.user.id) & Q(id=kwargs["pk"])).first()
        if not instance:
            return Response(data="No content", status=status.HTTP_204_NO_CONTENT)
        serializer = UtmSerializer(instance.utm)
        return Response(serializer.data)
