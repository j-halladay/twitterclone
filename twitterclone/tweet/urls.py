from django.contrib import admin
from django.urls import path
from twitterclone.tweet.views import tweet, CreateTweet
from django.contrib.auth.decorators import login_required
urlpatterns = [

    path('tweet/<int:id>', tweet),
    path('createtweet', login_required(CreateTweet.as_view())),
    # path('recipies/<int:id>', recipie),
    # path('author/<int:id>', author),
    # path('addauthor/', addauthor),
    # path('addrecipie/', addrecipie),
    # path('login/', loginpage),
    # path('logout/', logoutpage, name='logout')
]
