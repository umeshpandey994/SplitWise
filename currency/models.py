from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=10)
    symbol = models.CharField(max_length=10, null=True)
    conversion_rate = models.JSONField(null=True)

    def __str__(self):
        return f"{self.name}"
