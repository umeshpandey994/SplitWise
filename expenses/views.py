from django.db.models import Sum
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from expenses.models import Expenses
from expenses.serializers import ExpenseSerializer
from split.models import Split


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def listv2(self, request, *args, **kwargs):
        # Todo Improve this all query have a field on the expense table to
        #  point out the people who are part of the expenses
        expenses = Expenses.objects.all()
        expense_details = []

        for expense in expenses:
            if Split.objects.filter(expense=expense, user=request.user).exists():
                splits = Split.objects.filter(expense=expense)

                total_owed = 0.0
                total_receivable = 0.0

                # Calculate how much the logged-in user owes or will get back
                if expense.paid_by == request.user:
                    total_receivable += sum(splits.values_list("owes", flat=True))
                else:
                    total_owed += splits.filter(user=request.user).last().owes

                expense_details.append(
                    {
                        "paid_by": "Paid by you"
                        if expense.paid_by == request.user
                        else expense.paid_by.username,
                        "title": expense.title,
                        "total_amount": expense.total_amount,
                        "total_owed": total_owed,
                        "total_receivable": total_receivable,
                    }
                )
        return Response(expense_details, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        user = request.user
        expenses = Expenses.objects.filter(split__user=user).distinct()

        if not expenses.exists():
            return Response(
                {"message": "No expenses found for the user."},
                status=status.HTTP_404_NOT_FOUND,
            )
        expenses = expenses.prefetch_related("split_set")

        expense_details = []
        for expense in expenses:
            splits = expense.split_set.all()

            total_receivable = (
                splits.aggregate(receivable=Sum("owes")).get("receivable", 0.0)
                if expense.paid_by == user
                else 0.0
            )

            user_split = splits.filter(user=user).first()
            total_owed = user_split.owes if user_split else 0.0

            expense_details.append(
                {
                    "paid_by": "Paid by you"
                    if expense.paid_by == user
                    else expense.paid_by.username,
                    "title": expense.title,
                    "total_amount": round(expense.total_amount, 2),
                    "total_owed": round(total_owed, 2),
                    "total_receivable": round(total_receivable, 2)
                    if total_receivable
                    else 0.0,
                }
            )

        return Response(expense_details, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="user-outstanding_old")
    def get_user_outstanding_balance_old(self, request, *args, **kwargs):
        user = request.user
        # Todo Improve this all query have a field on the expense table to
        #  point out the people who are part of the expenses
        expenses = Expenses.objects.all()

        total_outstanding = 0.0
        breakdown = []

        for expense in expenses:
            total_receivable = 0
            total_owes = 0
            splits = Split.objects.filter(expense=expense, user=user)
            if splits.exists():
                if expense.paid_by == user:
                    total_receivable = sum(
                        Split.objects.filter(expense=expense).values_list(
                            "owes", flat=True
                        )
                    )
                    total_outstanding += total_receivable
                else:
                    total_owes = sum(
                        splits.filter(user=user).values_list("owes", flat=True)
                    )
                    total_outstanding -= total_owes

                breakdown.append(
                    {
                        "expense_id": expense.id,
                        "title": expense.title,
                        "paid_by": "Paid by you"
                        if expense.paid_by == user
                        else expense.paid_by.username,
                        "total_amount": expense.total_amount,
                        "total_owes": total_owes,
                        "total_receivable": total_receivable,
                    }
                )

        return Response(
            {
                "user": user.username,
                "total_outstanding": total_outstanding,
                "breakdown": breakdown,
            },
            status=status.HTTP_200_OK,
        )

    @action(detail=False, methods=["get"], url_path="user-outstanding")
    def get_user_outstanding_balance(self, request, *args, **kwargs):
        user = request.user
        # Fetch expenses where the user is part of the splits
        expenses = Expenses.objects.filter(split__user=user).distinct()

        if not expenses.exists():
            return Response(
                {"message": "No outstanding balances found for the user."},
                status=status.HTTP_404_NOT_FOUND,
            )

        expenses = expenses.prefetch_related("split_set")

        total_outstanding = 0.0
        breakdown = []

        for expense in expenses:
            splits = expense.split_set.all()
            total_receivable = 0.0
            total_owes = 0.0

            if expense.paid_by == user:
                # If user paid for the expense, calculate total receivable
                total_receivable = (
                    splits.aggregate(receivable=Sum("owes"))["receivable"] or 0.0
                )
                total_outstanding += total_receivable
            else:
                # Calculate the total the user owes
                user_split = splits.filter(user=user).first()
                total_owes = user_split.owes if user_split else 0.0
                total_outstanding -= total_owes

            breakdown.append(
                {
                    "expense_id": expense.id,
                    "title": expense.title,
                    "paid_by": "Paid by you"
                    if expense.paid_by == user
                    else expense.paid_by.username,
                    "total_amount": round(expense.total_amount, 2),
                    "total_owes": round(total_owes, 2),
                    "total_receivable": round(total_receivable, 2),
                }
            )

        return Response(
            {
                "user": user.username,
                "total_outstanding": round(total_outstanding, 2),
                "breakdown": breakdown,
            },
            status=status.HTTP_200_OK,
        )
