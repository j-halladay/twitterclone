from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class TwitterUser(models.Model):
    name = models.CharField(max_length=40)
    bio = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followed = models.ManyToManyField('TwitterUser', blank=True)
