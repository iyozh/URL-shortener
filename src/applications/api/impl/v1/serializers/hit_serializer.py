from rest_framework.serializers import ModelSerializer

from applications.statistics.models import Hit


class HitSerializer(ModelSerializer):
    class Meta:
        model = Hit
        fields = "__all__"
