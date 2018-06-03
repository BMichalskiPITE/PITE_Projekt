from user import views as user_views
from place import views as place_views
from trip import views as trip_views
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/sync/places/$', place_views.PlaceSyncView.as_view({'get': 'sync'}), name='places-list'),
    url(r'^api/places/$', place_views.PlaceView.as_view(), name='places-list'),
    url(r'^api/users/$', user_views.UserView.as_view(), name='users-list'),
    url(r'^api/trips/$', trip_views.TripView.as_view(), name='trips-list'), 
    url(r'^api/places/(?P<placeId>.+)/$', place_views.PlaceRudView.as_view(), name='places-rud'), 
    url(r'^api/users/(?P<id>.+)/$', user_views.UserRudView.as_view(), name='users-rud'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^api/trips/(?P<pk>.+)/$', trip_views.TripRudView.as_view(), name='trips-rud'),
    url(r'^api/orders/$', trip_views.trip_announce_list, name='trip-orders'),
    url(r'^api/acceptations/$', trip_views.trip_acceptation_list, name='trip-acceptations'),
    url(r'^api/messages', user_views.MessagesView.as_view(), name='messages-list'),
    url(r'^admin/', admin.site.urls),
]
