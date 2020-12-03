from django.conf.urls import url
from django.urls import path

from djangologin.views import abc

urlpatterns = [
    path('home/', abc, name="home"),

]