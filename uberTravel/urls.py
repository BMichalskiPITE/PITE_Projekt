"""uberTravel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from api import views
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/places/$', views.PlaceView.as_view(), name='places-list'),
    url(r'^api/users/$', views.UserView.as_view(), name='users-list'),
    url(r'^api/trips/$', views.TripView.as_view(), name='trips-list'), 
    url(r'^api/places/(?P<placeId>.+)/$', views.PlaceRudView.as_view(), name='places-rud'), 
    url(r'^api/users/(?P<user_id>.+)/$', views.UserRudView.as_view(), name='users-rud'),
    url(r'^api/trips/(?P<pk>.+)/$', views.TripRudView.as_view(), name='trips-rud'), 
    url(r'^admin/', admin.site.urls),
]