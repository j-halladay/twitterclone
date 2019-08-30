from django.db import models
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.models import Tweet


class Notification(models.Model):
    name = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tweet_id = models.IntegerField()
    text = models.CharField(max_length=140)
    # viewed = models.BooleanField(default=False)
