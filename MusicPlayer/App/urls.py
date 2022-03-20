
"""MusicPlayer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

"""




from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import UserRegisterView




app_name = "App"

urlpatterns = [
    path("", views.home, name="main"),
    path("home", views.home, name="home"),
    path("music", views.music, name="music"),
    path("contact", views.contact, name="contact"),
    path("search_songs", views.search_songs, name="search_songs"),
    path("show_music/<song_id>", views.show_music, name="show_music"),
    path("login", views.login, name="login"),
    path("signup", UserRegisterView.as_view(), name="signup"),

]