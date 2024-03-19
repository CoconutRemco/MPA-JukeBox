from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Make login page as the main page
    path('register/', views.register, name='register'),
    path('jukebox/', views.jukebox, name='jukebox'),
]
