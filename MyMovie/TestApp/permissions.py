from rest_framework import permissions
from django.http import Http404
from TestApp.models import *
from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):
    message = "You cant rate it "

    def has_permission(self, request, view):
        movie = Movie.objects.get(pk=request.data['movie'])
        user = request.data['user']
        ratings = Rating.objects.filter(movie=request.data['movie'], user=user)
        if movie.added_by == user:
            return False
        elif request.method in SAFE_METHODS and not ratings.exists():
            return True
        else:
            return False
