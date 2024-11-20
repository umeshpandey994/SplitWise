from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import BalanceData, User
from users.Serializer import BalanceDataSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class BalanceDataViewSet(viewsets.ModelViewSet):
    queryset = BalanceData.objects.all()
    serializer_class = BalanceDataSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id", None)
        currency_id = self.request.query_params.get("currency_id", None)

        if user_id and currency_id:
            return BalanceData.objects.filter(user_id=user_id, currency_id=currency_id)
        return BalanceData.objects.all()

    def update(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        currency_id = request.data.get("currency_id")
        outstanding_balance = request.data.get("outstanding_balance")

        balance_data, created = BalanceData.objects.get_or_create(
            user_id=user_id, currency_id=currency_id
        )
        balance_data.outstanding_balance = outstanding_balance
        balance_data.save()

        return Response(
            {"detail": "Balance updated successfully."}, status=status.HTTP_200_OK
        )
