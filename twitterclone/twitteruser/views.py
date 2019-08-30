from django.shortcuts import render
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.forms import AddUser
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied


def profile(request, id, *args, **kwargs):
    html = 'profile.html'
    item = TwitterUser.objects.get(id=id)
    items = Tweet.objects.all().filter(twitteruser=item)
    return render(request, html, {'userprofile': item, "tweets": items})


def follow(request, id, *args, **kwargs):
    if request.user.twitteruser != TwitterUser.objects.get(id=id):

        u = TwitterUser.objects.get(id=id)
        u.followed.add(request.user.twitteruser)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unfollow(request, id, *args, **kwargs):
    if request.user.twitteruser != TwitterUser.objects.get(id=id):
        u = TwitterUser.objects.get(id=id)
        u.followed.remove(
            request.user.twitteruser)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def adduser(request, *args, **kwargs):
    html = 'genericform.html'
    if request.method == "POST":
        form = AddUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(
                username=data['username'], password=data['password']
            )
            a = TwitterUser.objects.create(
                user=u, name=data['name'], bio=data['bio'])
            login(request, u)
            return HttpResponseRedirect(reverse('index'))
    form = AddUser()

    return render(request, html, {'form': form})
