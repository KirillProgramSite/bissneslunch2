from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(('номер телефона'), max_length=14)
    place = models.CharField(('место работы'), max_length=50)

# Create your models here.
