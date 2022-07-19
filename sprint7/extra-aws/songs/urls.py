from django.urls import path

from . import views

urlpatterns = [
    path("songs/", views.ListCreateSongView.as_view()),
]
