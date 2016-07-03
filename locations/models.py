from __future__ import unicode_literals

from django.db import models

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
