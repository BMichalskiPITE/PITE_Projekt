from django.apps import AppConfig


class PlaceConfig(AppConfig):
    name = 'place'
    google_maps_api_key = "AIzaSyDXJPkrTmAaD6AhH_7vFHBYxOEB1KZdqWo"
    google_maps_sync_location = "50.062533,19.93732"
    google_maps_sync_radius = "15000"
    google_maps_sync_type = "museum"
    google_maps_sync_max_pages = 5
    google_maps_interval_sec = 5