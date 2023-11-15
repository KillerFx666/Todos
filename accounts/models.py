from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    Phone_number = models.CharField(max_length=11, unique=True)
