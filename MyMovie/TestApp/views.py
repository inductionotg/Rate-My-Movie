"""from rest_framework import generics, viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from TestApp.serializer import UserSerializer, RegisterSerializer, UserMovieSerializer, RateSerializer,JoinModelSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.viewsets import ModelViewSet
from TestApp.models import *
from rest_framework.generics import ListAPIView
from django.shortcuts import render, redirect

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return redirect('http://127.0.0.1:8000/jointview/')
        return super(LoginAPI, self).post(request, format=None)

        # return HttpResponseRedirect(redirect_to='api/movie')


# Create your views here.
class UserMovieView(ModelViewSet):

    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = UserMovie.objects.all()
    serializer_class = UserMovieSerializer

class RatingRatesView(viewsets.ModelViewSet):
    serializer_class = RateSerializer

    def get_queryset(self):
        rates = RatingRates.objects.all()
        return rates
class JointView(ListAPIView):
    queryset = UserMovie.objects.raw(
        'select TestApp_usermovie.id,TestApp_usermovie.Movie,TestApp_usermovie.Title,TestApp_ratingrates.Rating from TestApp_usermovie  inner join TestApp_ratingrates on TestApp_usermovie.id=TestApp_ratingrates.id')
    serializer_class = JoinModelSerializer

"""
from urllib import request

from django.contrib.auth import login
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from knox.models import AuthToken

from TestApp.models import Movie, Rating
from TestApp.serializer import UserSerializer, RegisterSerializer, LoginSerializer, MovieSerializer, RatingSerializer
from TestApp.permissions import UserPermission


class UserAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class MovieAPIView(generics.ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()

    @permission_classes([IsAuthenticated])
    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)



class RatingAPIView(generics.CreateAPIView):
    serializer_class = RatingSerializer

    @permission_classes([IsAuthenticated,UserPermission])
    def perform_create(self, serializer):

        serializer.save(user=self.request.user)









