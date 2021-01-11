from rest_framework import permissions
from django.http import Http404
from TestApp.models import *
from rest_framework.permissions import BasePermission, SAFE_METHODS

"""
class UserPermission(BasePermission):

    
    message= "Allow users who have not added the movie to rate the movie once."
    def has_permission(self, request, view):
        try:
            movie = Movie.objects.get(pk=request.data['movie'])
        except Movie.DoesNotExist:
            raise Http404

        if request.user != movie.added_by:
            try:
                Rating.objects.get(movie=request.data['movie'], user=request.user)
                return False
            except Rating.DoesNotExist:
                return True
        return False
"""


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
