from rest_framework import serializers
from django.contrib.auth.models import User
from TestApp.models import UserMovie


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

        def get_serializer_context(self):
            return {'Rating': self.kwargs['Rating'], 'request': self.request}


    def validate(self, data):
        Rating = self.context["Rating"]
        if UserMovie.objects.filter(Rating=Rating, username=self.context["request"].user).exists():
            raise serializers.ValidationError("This user has already added rating")
        return data
class UserMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserMovie
        fields='__all__'

