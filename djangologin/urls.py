from django.conf.urls import url
from django.urls import path

from djangologin.views import abc, abc2, abc3

urlpatterns = [
    path('home/', abc, name="home"),
    path('bike/', abc2, name="bike"),
    path('bicycle/', abc3, name="bicycle"),

]