from django.contrib.auth.models import AbstractUser
from django.db import models


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
