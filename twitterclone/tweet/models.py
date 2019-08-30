from django.db import models
from twitterclone.twitteruser.models import TwitterUser


class Tweet(models.Model):
    text = models.CharField(max_length=140)
    twitteruser = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
