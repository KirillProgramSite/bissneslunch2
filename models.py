from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    number = models.CharField(("номер телефона"), max_length=15, null=True, blank=True)
    place = models.CharField(("место работы"), max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username