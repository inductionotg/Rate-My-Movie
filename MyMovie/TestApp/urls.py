from django.urls import path, include

from knox.views import LogoutView

from TestApp.views import UserAPIView, RegisterAPIView, LoginAPIView, MovieApi, RatingApi
# RatingAPIView,MovieAPIView

from TestApp import views

urlpatterns = [
    path('', include('knox.urls')),
    path('user', UserAPIView.as_view()),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutView.as_view(), name='knox_logout'),
    path('movies', views.MovieApi.as_view()),
    path('rating', views.RatingApi.as_view())
]
