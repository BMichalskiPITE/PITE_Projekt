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
from user import views as user_views
from place import views as place_views
from trip import views as   trip_views
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/places/$', place_views.PlaceView.as_view(), name='places-list'),
    url(r'^api/users/$', user_views.UserView.as_view(), name='users-list'),
    url(r'^api/trips/$', trip_views.TripView.as_view(), name='trips-list'), 
    url(r'^api/places/(?P<placeId>.+)/$', place_views.PlaceRudView.as_view(), name='places-rud'), 
    url(r'^api/users/(?P<id>.+)/$', user_views.UserRudView.as_view(), name='users-rud'),
    url(r'^api/trips/(?P<pk>.+)/$', trip_views.TripRudView.as_view(), name='trips-rud'), 
    url(r'^admin/', admin.site.urls),
]