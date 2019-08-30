"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitterclone.authentication.urls import urlpatterns as authpatterns
from twitterclone.notification.urls import urlpatterns as notifpatterns
from twitterclone.tweet.urls import urlpatterns as tweetpatterns
from twitterclone.twitteruser.urls import urlpatterns as tupatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name='index'),
    # path('recipies/<int:id>', recipie),
    # path('author/<int:id>', author),
    # path('addauthor/', addauthor),
    # path('addrecipie/', addrecipie),
    # path('login/', loginpage),
    # path('logout/', logoutpage, name='logout')
]
urlpatterns += authpatterns
urlpatterns += notifpatterns
urlpatterns += tweetpatterns
urlpatterns += tupatterns
