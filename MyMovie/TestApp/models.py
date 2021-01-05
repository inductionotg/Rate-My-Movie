'''from django.db import models


# Create your models here.
class RatingRates(models.Model):
    Rating = models.IntegerField()

class UserMovie(models.Model):
    Movie = models.CharField(max_length=64)
    Title = models.CharField(max_length=128)
    #rates = models.OneToOneField(RatingRates, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Movie

class JoinModel(models.Model):
    Movie=models.CharField(max_length=64)
    Title=models.CharField(max_length=128)
    Rating=models.IntegerField()
'''

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.CharField(max_length=128)
    added_by = models.ForeignKey(User, related_name="movie", on_delete=models.CASCADE, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    # rating=models.IntegerField()
    class Meta:
        db_table = "Movie"

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rating')

    class Meta:
        db_table = "Rating"


