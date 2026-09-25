from django.urls import path
from . import views 

#app_name="lastfm"
urlpatterns = [
    path('',views.home, name='home'),
    path('top-artists/', views.topartistsv, name='top_artists'),
    path('top-tracks/', views.toptracksv, name='top_tracks'),
    path('search/artist/', views.artistsearchv, name='artist_search'),
    path('search/album/', views.albumsearchv, name='album_search'),
    path('search/track/', views.tracksearchv, name='track_search'),
]



