from django.db import models

from currency.models import Currency
from users.models import User


class Expenses(models.Model):
    paid_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="expenses_paid_by"
    )
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    total_amount = models.FloatField(
        help_text="This will store the total expense amount"
    )
    title = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.currency.name} {self.total_amount}"


class Split(models.Model):
    expense = models.ForeignKey(Expenses, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owes = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owes}"
