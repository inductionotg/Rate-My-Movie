from rest_framework import serializers
from django.contrib.auth.models import User
from TestApp.models import UserMovie, RatingRates


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


class UserMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMovie
        fields = ['id', 'Movie', 'Title','rates']


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingRates
        fields = ['id', 'Rating', ]


"""class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingRates
        fields = ('Rating',)"""
