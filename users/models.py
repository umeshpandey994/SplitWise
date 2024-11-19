from django.contrib.auth.models import AbstractUser
from django.db import models

from currency.models import Currency


class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Attributes:
        phone_number (str): A unique phone number for the user.
    """

    phone_number = models.CharField(
        max_length=13,
        unique=True,
        blank=True,
        help_text="User phone number must be unique across users",
    )

    def __str__(self):
        return f"{self.username}"


class Group(models.Model):
    pass


class BalanceData(models.Model):
    """
    To manage multi currency outstanding balance
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    outstanding_balance = models.FloatField(default=0.00)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} - {self.outstanding_balance}"

    class Meta:
        unique_together = ("user", "currency")
