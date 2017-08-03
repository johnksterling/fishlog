from __future__ import unicode_literals

from django.db import models
from locations.models import Location
from django.contrib.auth.models import User


class Trip(models.Model):
    description = models.CharField(max_length=200)
    trip_date = models.DateTimeField('trip date')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    comments = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.description


class TripImage(models.Model):
    trip = models.ForeignKey(Trip, related_name='images')
    image = models.ImageField()
