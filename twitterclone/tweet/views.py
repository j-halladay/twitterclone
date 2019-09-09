from django.shortcuts import render
from twitterclone.tweet.models import Tweet
from twitterclone.notification.models import Notification
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.forms import CreateTweet
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
import re
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView


def tweet(request, id, *args, **kwargs):
    html = 'tweet.html'
    item = Tweet.objects.get(id=id)
    profile = item.twitteruser
    print(item.twitteruser.name)
    return render(request, html, {'tweet': item, "userprofile": profile})


@login_required
def createtweet(request, *args, **kwargs):
    html = 'genericform.html'
    if request.method == "POST":
        form = CreateTweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = request.user.twitteruser
            a = Tweet.objects.create(
                twitteruser=u, text=data['text'])
            atuser = re.compile('@([a-zA-Z0-9]*)')
            found = re.search(atuser, data['text'])
            if found:
                print('help')
                found = found.group(0).replace('@', '').strip()
                if TwitterUser.objects.get(name=found):
                    u = TwitterUser.objects.get(name=found)
                    Notification.objects.create(
                        name=u, tweet_id=a.id, text=a.text
                    )
            return HttpResponseRedirect(reverse('index'))

    form = CreateTweet()

    return render(request, html, {'form': form})


class MakeTweet(TemplateView):
    html = 'genericform.html'
    def post(self, request, *args, **kwargs):

        form = CreateTweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = request.user.twitteruser
            a = Tweet.objects.create(
                twitteruser=u, text=data['text'])
            atuser = re.compile('@([a-zA-Z0-9]*)')
            found = re.search(atuser, data['text'])
            if found:
                print('help')
                found = found.group(0).replace('@', '').strip()
                if TwitterUser.objects.get(name=found):
                    u = TwitterUser.objects.get(name=found)
                    Notification.objects.create(
                        name=u, tweet_id=a.id, text=a.text
                    )
            return HttpResponseRedirect(reverse('index'))

    def get(self, request, *args, **kwargs):
        form = CreateTweet()

        return render(request, self.html, {'form': form})
