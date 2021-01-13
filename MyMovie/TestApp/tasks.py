from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from TestApp.models import Movie, Rating,User


@shared_task
def send_rating():

    rating = Rating.objects.all()
    body = rating.rating
    to = [User.email, ]
    sender = settings.EMAIL_HOST_USER
    subject = "Ratings of the movie are"
    send_mail(subject, body, sender, to, fail_silently=False)

