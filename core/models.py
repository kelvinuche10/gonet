from django.db import models
from datetime import datetime


class Room(models.Model):
    name = models.CharField(max_length=100)


class Messages(models.Model):
    value = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now)
    user = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.user
