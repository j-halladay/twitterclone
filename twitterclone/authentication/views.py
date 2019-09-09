from django.shortcuts import render
from twitterclone.tweet.models import Tweet
from twitterclone.authentication.forms import LoginForm
from twitterclone.notification.models import Notification
from twitterclone.twitteruser.models import TwitterUser
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView


def index(request, *args, **kwargs):
    html = 'index.html'
    if not request.user.is_anonymous:
        u = TwitterUser.objects.get(name=request.user.twitteruser.name)
        notify = Notification.objects.all().filter(name=u)

        tweets = Tweet.objects.all()
        mytweets = Tweet.objects.all().filter(twitteruser=request.user.twitteruser)
        followed_tweets = []
        for i in tweets:
            if request.user.twitteruser in i.twitteruser.followed.all():
                followed_tweets.append(i)
        followed_tweets += mytweets
        return render(request, html, {"notifications": notify, "tweets": followed_tweets})
    else:
        return render(request, html)


def loginpage(request, *args, **kwargs):
    html = 'genericform.html'

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = authenticate(
                username=data['username'], password=data['password'])
            if u is not None:
                login(request, u)
            else:
                return HttpResponseRedirect(reverse('login'))
            destination = request.GET.get('next')
            if destination is not None:
                return HttpResponseRedirect(destination)
            else:
                return HttpResponseRedirect(reverse('index'))
    form = LoginForm()

    return render(request, html, {'form': form})


class LoginPage(TemplateView):
    html = 'genericform.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()

        return render(request, self.html, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = authenticate(
                username=data['username'], password=data['password'])
            if u is not None:
                login(request, u)
            else:
                return HttpResponseRedirect(reverse('login'))
            destination = request.GET.get('next')
            if destination is not None:
                return HttpResponseRedirect(destination)
            else:
                return HttpResponseRedirect(reverse('index'))


def logoutpage(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))


class LogoutPage(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)

        return HttpResponseRedirect(reverse('index'))
