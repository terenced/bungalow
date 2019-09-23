from api.core.models import Metadata
from api.core.serializers import MetadataSerializer
from rest_framework import viewsets


class MetadataViewSet(viewsets.ModelViewSet):
    queryset = Metadata.objects.all().order_by('-updated_at')
    serializer_class = MetadataSerializer
