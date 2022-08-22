from ctypes import addressof
from ssl import create_default_context
from types import CoroutineType
from unicodedata import name
from django.db import models


class Company(models.Model):
    name = models.CharField(50)
    description = models.TextField()
    address = models.CharField(125)
    city = models.CharField(30)
    region = models.CharField(30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
