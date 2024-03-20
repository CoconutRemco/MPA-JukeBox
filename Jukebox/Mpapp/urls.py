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
]
