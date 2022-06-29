from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from parking_lots.permissions import IsOwnerOrReadOnly
from parking_lots.serializers import (
    DetailParkingLotSerializer,
    ListParkingLotSerializer,
)

from .mixins import SerializerByMethodMixin
from .models import ParkingLot


class ListCreateParkingLotView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = ParkingLot.objects.all()
    serializer_map = {
        "GET": ListParkingLotSerializer,
        "POST": DetailParkingLotSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RetrieveUpdateDestroyParkingLotView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = ParkingLot.objects.all()
    serializer_class = DetailParkingLotSerializer
