from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name
