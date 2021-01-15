from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from TestApp.models import Movie, Rating,User
from django.db.models import Avg

@shared_task
def send_rating():
    body= Rating.objects.all().aggregate(Avg('rating'))
    to = [User.email, ]
    sender = settings.EMAIL_HOST_USER
    subject = "Ratings of the movie are"
    send_mail(subject, body, sender, to, fail_silently=False)

@shared_task
def send_email(email):
    u=Rating.objects.all().aggregate(Avg('rating'))
    print(f'rating {u}')
    print(f'A sample mail {email}')

