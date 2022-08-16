from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Pessoa(AbstractUser):
    bio = models.TextField(max_length=100, null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)

    def diga_ola(self):
        return "Hello, World. Utilizando Abstact User"