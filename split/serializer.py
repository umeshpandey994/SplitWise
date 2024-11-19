from rest_framework import serializers

from split.models import Split


class SplitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Split
        fields = ["expense", "user", "owes", "created_at"]
