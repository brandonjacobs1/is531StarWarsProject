import os.path

from django.db import models
from starWars.storage_backends import PublicMediaStorage


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField(default=None, blank=True, null=True)
    image = models.ImageField(storage=PublicMediaStorage(), default=None, blank=True, null=True)

    def __str__(self):
        return self.name

