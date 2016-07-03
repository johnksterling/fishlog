from __future__ import unicode_literals

from django.db import models
from locations.models import Location

class Trip(models.Model):
    description = models.CharField(max_length=200)
    trip_date = models.DateTimeField('trip date')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    comments = models.TextField()
    def __str__(self):
        return self.description


