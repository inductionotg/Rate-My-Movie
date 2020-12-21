from django.db import models


# Create your models here.
class RatingRates(models.Model):
    Rating = models.BigIntegerField(default=0)

class UserMovie(models.Model):
    Movie = models.CharField(max_length=64)
    Title = models.CharField(max_length=128)
    rates = models.OneToOneField(RatingRates, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Movie
