from api.core.models import Listing
from api.core.serializers.metadata import MetadataSerializer
from api.core.serializers.sales_history import SalesHistorySerializer

from rest_framework import serializers


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    sales_history = SalesHistorySerializer(
        many=True,
        read_only=True,
        source='saleshistory_set',
    )
    
    metadata = MetadataSerializer(
        many=True,
        read_only=True,
        source='metadata_set'
    )

    class Meta:
        model = Listing
        fields = "__all__"
