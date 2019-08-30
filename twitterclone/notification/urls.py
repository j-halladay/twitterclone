from django.contrib import admin
from django.urls import path
from twitterclone.notification.views import viewed

urlpatterns = [
    path('viewed/<int:id>', viewed),
    # path('', index, name='index'),
    # path('recipies/<int:id>', recipie),
    # path('author/<int:id>', author),
    # path('addauthor/', addauthor),
    # path('addrecipie/', addrecipie),
    # path('login/', loginpage),
    # path('logout/', logoutpage, name='logout')
]
