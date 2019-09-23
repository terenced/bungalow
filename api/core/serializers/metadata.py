from rest_framework import serializers

from api.core.models import Metadata


class MetadataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Metadata
        fields = "__all__"
