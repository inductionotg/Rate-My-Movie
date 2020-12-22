from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.CharField(max_length=128)
    added_by = models.ForeignKey(User, related_name="movies", on_delete=models.CASCADE, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
