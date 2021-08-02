from django.db.models import Q
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from applications.api.impl.v1.serializers.hit_serializer import HitSerializer
from applications.statistics.models import Hit


class HitViewSet(mixins.ListModelMixin, GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = HitSerializer

    def get_queryset(self):
        queryset = Hit.objects.filter(
            Q(link__user_id=self.request.user.id)
            & Q(link_id=self.request.query_params["id"])
        )
        return queryset
