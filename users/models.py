from django.db import models
from django.contrib.auth.models import AbstractUser

from business.models import Empresa

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(
        max_length=100, unique=True, blank=True, null=True
    )
    business = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        null=True, blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

