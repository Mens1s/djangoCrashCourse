from django.db import models


# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    l = models.CharField(max_length=10, blank=True)
