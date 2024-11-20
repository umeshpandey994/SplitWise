from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from currency.models import Currency
from currency.serializers import CurrencySerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticated]
