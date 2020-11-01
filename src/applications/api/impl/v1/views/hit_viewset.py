from django.db.models import Q
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from applications.api.impl.v1.serializers.hit_serializer import HitSerializer
from applications.statistics.models import Hit


class HitViewSet(mixins.ListModelMixin, GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = HitSerializer
    queryset = Hit.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Hit.objects.filter(
            Q(link__user_id=self.request.user.id)
            & Q(link_id=request.query_params["id"])
        )
        serializer = HitSerializer(queryset, many=True)
        return Response(serializer.data)
