import secrets

from django.db.models import Q
from dynaconf import settings as _ds
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from applications.api.impl.v1.serializers.link_serializer import LinkSerializer
from applications.homepage.models import Link
from applications.statistics.models import UTM


class LinkViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

    def perform_create(self, serializer):
        shortcut = _ds.PROTOCOL_HOST + secrets.token_urlsafe(3)
        user_id = self.request.user.id
        utm_copy = self.request.POST["original"]
        serializer.save(
            shortcut=shortcut, user_id=user_id, utm_copy=utm_copy, marker=True
        )
        utm = UTM(link_id=serializer.data["id"])
        utm.save()

    def list(self, request, *args, **kwargs):
        queryset = Link.objects.filter(user_id=self.request.user.id)
        serializer = LinkSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = Link.objects.filter(
            Q(user_id=self.request.user.id) & Q(id=kwargs["pk"])
        ).first()

        if not instance:
            return Response(data="Not found", status=status.HTTP_404_NOT_FOUND)

        return super().retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        instance = Link.objects.filter(
            Q(user_id=self.request.user.id) & Q(id=kwargs["pk"])
        ).first()

        if not instance:
            return Response(data="Not found", status=status.HTTP_404_NOT_FOUND)

        return super().partial_update(request, *args, **kwargs)
