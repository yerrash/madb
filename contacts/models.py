from django.db import models


class Contact(models.Model):
    departament_responsible = models.CharField(max_length=50)
    number = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=50, null=True)
    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="contacts",
        null=True,
    )
