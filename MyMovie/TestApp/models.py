from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.CharField(max_length=128)
    added_by = models.ForeignKey(User, related_name="movie", on_delete=models.CASCADE, null=True)
    added_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "Movie"


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rating')

    class Meta:
        db_table = "Rating"
