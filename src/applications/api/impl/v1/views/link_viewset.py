import secrets

from dynaconf import settings as _ds
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from applications.api.impl.v1.serializers.link_serializer import LinkSerializer
from applications.homepage.models import Link
from applications.statistics.models import UTM


class LinkViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LinkSerializer

    def get_queryset(self):
        queryset = Link.objects.filter(user_id=self.request.user.id)
        return queryset

    def perform_create(self, serializer):
        shortcut = _ds.PROTOCOL_HOST + secrets.token_urlsafe(3)
        user_id = self.request.user.id
        utm_copy = self.request.POST["original"]
        serializer.save(
            shortcut=shortcut, user_id=user_id, utm_copy=utm_copy, marker=True
        )
        utm = UTM(link_id=serializer.data["id"])
        utm.save()


