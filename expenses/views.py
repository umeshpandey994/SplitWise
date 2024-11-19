from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from expenses.models import Expenses
from expenses.serializers import ExpenseSerializer
from split.models import Split
from users.models import User


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer

    def list(self, request, *args, **kwargs):
        data = []
        expenses = Expenses.objects.all().prefetch_related("split_set")

        for expense in expenses:
            total_owes = sum(split.owes for split in expense.split_set.all())

            data.append(
                {
                    "id": expense.id,
                    "paid_by": expense.paid_by.username,
                    "total_paid": expense.total_amount,
                    "outstanding": expense.total_amount - total_owes,
                    "title": expense.title,
                }
            )

        return Response(data)

    @action(detail=False, methods=["get"], url_path="user-outstanding")
    def get_user_outstanding_balance(self, request, *args, **kwargs):
        user_id = request.query_params.get("user_id")

        # Get the user object
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=404)

        expenses = Expenses.objects.all()
        total_outstanding = 0.0
        breakdown = []

        for expense in expenses:
            splits = Split.objects.filter(expense=expense, user=user)
            if splits.exists():
                total_owes = Split.objects.filter(expense=expense).values_list(
                    "owes", flat=True
                )

                total_owes_sum = sum(total_owes)

                outstanding_balance = expense.total_amount - total_owes_sum

                breakdown.append(
                    {
                        "expense_id": expense.id,
                        "title": expense.title,
                        "paid_by": "Paid by you"
                        if expense.paid_by == user
                        else expense.paid_by.username,
                        "total_amount": expense.total_amount,
                        "total_owes": total_owes_sum,
                        "outstanding": outstanding_balance,
                    }
                )

                if expense.paid_by == user:
                    total_outstanding += total_owes_sum
                else:
                    total_outstanding -= outstanding_balance

        return Response(
            {
                "user": user.username,
                "total_outstanding": total_outstanding,
                "breakdown": breakdown,
            }
        )
