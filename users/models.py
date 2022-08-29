from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import CustomUserManager


class Status(models.TextChoices):
    ACADEMIC = ("Acadêmico",)
    CONTRIBUTOR = ("Contribuidor",)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CONTRIBUTOR,
    )

    username = None
    is_staff = None

    objects = CustomUserManager()
    REQUIRED_FIELDS = ["first_name", "last_name"]
    USERNAME_FIELD = "email"
