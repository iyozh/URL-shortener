from rest_framework.serializers import ModelSerializer

from applications.homepage.models import Link
from applications.statistics.models import UTM


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"

    def save(self, **kwargs):
        instance = super().save(**kwargs)

        utm = UTM(link_id=self.instance.id)
        utm.save()

        return instance
