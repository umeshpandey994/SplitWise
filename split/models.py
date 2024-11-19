from django.db import models

from expenses.models import Expenses
from users.models import User


class Split(models.Model):
    expense = models.ForeignKey(Expenses, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owes = models.FloatField(default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owes}"
