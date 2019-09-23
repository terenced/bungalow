from api.core.models import SalesHistory
from api.core.serializers import SalesHistorySerializer
from rest_framework import viewsets


class SalesHistoryViewSet(viewsets.ModelViewSet):
    queryset = SalesHistory.objects.all().order_by('-updated_at')
    serializer_class = SalesHistorySerializer
