from ctypes import addressof
from ssl import create_default_context
from types import CoroutineType
from unicodedata import name
from django.db import models


class Company(models.Model):
    name = models.CharField(50)
    description = models.TextField()
    website = models.CharField(125, null=True)
    address = models.CharField(125)
    city = models.CharField(30)
    region = models.CharField(30)
    products = models.ManyToManyField("products.Product", related_name="companies")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
