from django.db import models


class Contact(models.Model):
    departament_responsible = models.CharField(50)
    number_email = models.CharField(30)
    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="contacts",
        null=True,
    )
