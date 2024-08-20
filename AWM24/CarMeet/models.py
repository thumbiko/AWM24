from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    coordinates = models.PointField()

'''
class CarMeet(models.Model):
        name = models.CharField(max_length=255)
        description = models.TextField()
        date = models.DateTimeField()
        location = models.PointField()
'''


def __str__(self):
        return self.name
