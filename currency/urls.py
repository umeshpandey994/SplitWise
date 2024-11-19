from django.urls import include, path
from rest_framework import routers

from currency.views import CurrencyViewSet

router = routers.DefaultRouter()
router.register(r"", CurrencyViewSet, basename="currency")

urlpatterns = [
    path("currency/", include(router.urls)),
]
