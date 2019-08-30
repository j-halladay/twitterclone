from django.shortcuts import render
from twitterclone.notification.models import Notification
from twitterclone.tweet.models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied


def viewed(request, id, *args, **kwargs):

    Notification.objects.get(tweet_id=id).delete()

    return HttpResponseRedirect('/tweet/'+str(id))
