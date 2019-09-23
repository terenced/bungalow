from rest_framework import serializers

from api.core.models import SalesHistory


class SalesHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SalesHistory
        fields = "__all__"
