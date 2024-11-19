from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ["id", "username", "email", "phone_number"]
        fields = "__all__"
