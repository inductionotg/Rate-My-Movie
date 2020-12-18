from django.db import models


# Create your models here.
class UserMovie(models.Model):
    Movie = models.CharField(max_length=64)
    Title = models.CharField(max_length=128)
    Rating = models.IntegerField()
