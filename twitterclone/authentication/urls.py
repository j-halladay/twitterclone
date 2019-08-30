from django.contrib import admin
from django.urls import path
from twitterclone.authentication.views import index, loginpage, logoutpage

urlpatterns = [
    path('login/', loginpage),
    path('logout/', logoutpage, name='logout'),
    path('', index, name='index')
]
