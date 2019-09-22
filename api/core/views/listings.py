from api.core.models import Listing
from api.core.serializers import ListingSerializer
from rest_framework import viewsets


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all().order_by('-updated_at')
    serializer_class = ListingSerializer
