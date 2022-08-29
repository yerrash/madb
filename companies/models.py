from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    website = models.CharField(max_length=125, null=True)
    address = models.CharField(max_length=125)
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    products = models.ManyToManyField("products.Product", related_name="companies")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
