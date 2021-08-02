from rest_framework.serializers import ModelSerializer

from applications.statistics.models import UTM


class UtmSerializer(ModelSerializer):
    class Meta:
        model = UTM
        fields = "__all__"
