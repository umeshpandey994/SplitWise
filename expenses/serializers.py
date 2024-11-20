from django.db import transaction
from rest_framework import serializers

from expenses.models import Expenses
from split.models import Split
from users.models import User

from .utils import calculate_split


class ExpenseSerializer(serializers.ModelSerializer):
    # Extra fields for split calculation
    users = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=True
    )
    split_type = serializers.ChoiceField(
        choices=["equal", "fixed", "percentage"], write_only=True, required=True
    )
    amounts = serializers.ListField(
        child=serializers.FloatField(), write_only=True, required=False
    )

    class Meta:
        model = Expenses
        fields = [
            "id",
            "paid_by",
            "currency",
            "total_amount",
            "title",
            "created_at",
            "updated_at",
            "users",
            "split_type",
            "amounts",
        ]
        extra_kwargs = {
            "users": {"write_only": True},
            "split_type": {"write_only": True},
            "amounts": {"write_only": True},
        }

    def validate(self, attrs):
        users = attrs.get("users")
        split_type = attrs.get("split_type")
        total_amount = attrs.get("total_amount")
        amounts = attrs.get("amounts")

        if len(users) != User.objects.filter(id__in=users).count():
            raise serializers.ValidationError({"users": "Please add the valid users."})

        if total_amount <= 0:
            raise serializers.ValidationError(
                {"total_amount": "Total amount should be in positive."}
            )

        if not users:
            raise serializers.ValidationError({"users": "User list cannot be empty."})

        if split_type not in ["equal", "fixed", "percentage"]:
            raise serializers.ValidationError({"split_type": "Invalid split type."})

        if amounts:
            if any(value < 0 for value in amounts):
                raise serializers.ValidationError(
                    {"amounts": "Values cannot contain negative numbers."}
                )

        return attrs

    def create(self, validated_data):
        users = validated_data.pop("users")
        split_type = validated_data.pop("split_type")
        amounts = validated_data.pop("amounts", [])

        expense = Expenses.objects.create(**validated_data)
        # import ipdb; ipdb.set_trace()
        try:
            split_data = calculate_split(expense, users, split_type, amounts)
        except ValueError as e:
            raise serializers.ValidationError({"detail": str(e)})

        paid_by_user = validated_data["paid_by"].id
        if paid_by_user in split_data:
            split_data[paid_by_user] = 0.0

        with transaction.atomic():
            splits = []
            for user_id, amount in split_data.items():
                split = Split(expense=expense, user_id=user_id, owes=amount)
                splits.append(split)
            Split.objects.bulk_create(splits)
        return expense
