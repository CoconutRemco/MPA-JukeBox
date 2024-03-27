from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Make login page as the main page
    path('register/', views.register, name='register'),
    path('jukebox/', views.jukebox, name='jukebox'),
    path('spotify_auth/', views.spotify_auth, name='spotify_auth'),
    path('spotify_callback/', views.spotify_callback, name='spotify_callback'),
    path('spotify_request/', views.spotify_request, name='spotify_request'),
    path('song/<str:song_id>/', views.song_detail, name='song_detail'),
    path('update_playlist/<int:playlist_id>/', views.update_playlist, name='update_playlist'),
    path('create_playlist/', views.create_playlist, name='create_playlist'),
    path('delete_playlist/<int:playlist_id>/', views.delete_playlist, name='delete_playlist'),
    path('delete_song_from_playlist/<int:playlist_id>/<int:song_id>/', views.delete_song_from_playlist, name='delete_song_from_playlist'),
    path('add_song_to_playlist/<int:playlist_id>/', views.add_song_to_playlist, name='add_song_to_playlist'),
    path('logout/', views.logout_view, name='custom_logout'),
]

