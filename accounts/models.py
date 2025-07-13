from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    city = models.CharField(max_length=255, blank=True, null=True)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

