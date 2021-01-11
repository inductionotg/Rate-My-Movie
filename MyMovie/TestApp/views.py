
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from knox.models import AuthToken
from rest_framework.views import APIView
from TestApp.models import Movie, Rating
from TestApp.serializer import UserSerializer, RegisterSerializer, LoginSerializer, MovieSerializer, RatingSerializer
from rest_framework import status
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



class MovieApi(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MovieSerializer

    def get(self, request, format=None):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(added_by=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RatingApi(APIView):
    permission_classes = (IsAuthenticated, UserPermission)
    serializer_class = RatingSerializer

    def get(self, request, format=None):
        rating = Rating.objects.all()
        serializer = RatingSerializer(rating, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        # request.data['user'] = self.request.user
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

