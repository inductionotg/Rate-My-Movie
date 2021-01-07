from rest_framework import permissions
from TestApp.models import *


class UserPermission(permissions.BasePermission):
    message = 'Adding ratings by same user not allowed.'

    def has_permission(self, request, view, attrs):
        allowed_methods = ['POST', 'PATCH']
        # validated_data = self.context['request'].movie
        user = self.context['request'].user
        ratings = Rating.objects.filter(movie=validated_data['movie'], user=user)
        if validated_data['movie'].added_by == user:
            return False
        elif request.method in SAFE_METHODS and not ratings.exists():
            return True
        else:
            return False

    '''def has_permission(self, request, view, attrs):
        allowed_methods = ['POST', 'PATCH']
        # validated_data = super().validate(attrs)
        #user = self.context['request'].user
        user = Movie.objects.get(id=added_by)
        movie=Rating.objects.get(id=user)
        if user==movie :

            #request.method in SAFE_METHODS and Rating.objects.filter(movie=movie_id, user=user).exists():
            return False
        else:
            return True
            '''


"""
class Add(BasePermission):
    def has_permission(self, request, view):
        allowed_methods = ['POST', 'PATCH']
        user = Movie.objects.get(id=user_id)
        t = Rating.objects.filter(added_by_id=user)
        if request.method in allowed_methods:
            if t == user:
                return False
            else:
                return True
        else:
            return True
"""

"""
class Add(BasePermission):
    def has_permission(self, request, view):
        validated_data = super().validate(attrs)
        user = self.context['request'].user
        if Rating.objects.filter(movie=validated_data['movie'], user=user).exists():
            raise serializers.ValidationError('User already rated the movie')
        return validated_data
"""
