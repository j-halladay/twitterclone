from django.contrib import admin
from django.urls import path
from twitterclone.authentication.views import index, LoginPage, LogoutPage

urlpatterns = [
    # path('login/', loginpage),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutPage.as_view(), name='logout'),
    path('', index, name='index')
]
