from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="equipments",
        null=True,
    )
