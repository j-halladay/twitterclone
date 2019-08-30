from django.contrib import admin
from django.urls import path
from twitterclone.twitteruser.views import adduser, profile, follow, unfollow
urlpatterns = [
    path('signup/', adduser),
    path('profile/<int:id>', profile),
    path('follow/<int:id>', follow),
    path('unfollow/<int:id>', unfollow),
    # path('', index, name='index'),
    # path('recipies/<int:id>', recipie),
    # path('author/<int:id>', author),
    # path('addauthor/', addauthor),
    # path('addrecipie/', addrecipie),
    # path('login/', loginpage),
    # path('logout/', logoutpage, name='logout')
]
