from django.shortcuts import render
from rest_framework import generics

from songs.serializers import SongSerializer

from .models import Song


# Create your views here.
class ListCreateSongView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
