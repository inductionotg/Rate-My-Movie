"""from rest_framework import serializers
from django.contrib.auth.models import User
from TestApp.models import UserMovie, RatingRates, JoinModel


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
        fields = ['id', 'Movie', 'Title']


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingRates
        fields = ['id', 'Rating', ]


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingRates
        fields = ('Rating',)


class JoinModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinModel
        fields = ['id', 'Movie', 'Rating', 'Title']
"""
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import serializers

from TestApp.models import Movie, Rating
from urllib import request


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Wrong Credentials")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'director']


class RatingSerializer(serializers.ModelSerializer):


    # id=MovieSerializer(read_only=True)




    class Meta:
        model = Rating
        fields = ['id', 'movie','rating']

