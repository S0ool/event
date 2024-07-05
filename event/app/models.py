from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


def validate_description(value):
    if len(value) < 10:
        raise ValidationError("Описание должно быть длиннее 10 символов")


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(validators=[validate_description])
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='events/%d-%m-%y')

    def __str__(self):
        return self.title


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    events = models.ManyToManyField(Event, related_name='participants')

    def __str__(self):
        return self.user.username
