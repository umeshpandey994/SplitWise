from rest_framework import serializers

from users.models import BalanceData, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "phone_number"]
        # fields = "__all__"


class BalanceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceData
        fields = ["user", "outstanding_balance", "currency"]
