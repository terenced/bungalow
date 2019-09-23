from django.urls import include, path
from rest_framework import routers

from api.core.views import (
    ListingViewSet,
    MetadataViewSet,
    SalesHistoryViewSet,
    UserViewSet,
)

router = routers.DefaultRouter()
router.register(r"listings", ListingViewSet)
router.register(r"users", UserViewSet)
router.register(r"metadata", MetadataViewSet)
router.register(r"sales_history", SalesHistoryViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
