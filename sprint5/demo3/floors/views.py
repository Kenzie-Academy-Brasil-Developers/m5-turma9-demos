from django.shortcuts import get_object_or_404, render
from parking_lots.models import ParkingLot
from rest_framework import generics

from floors.serializers import FloorSerializer

from .models import Floor


# Create your views here.
class ListCreateFloor(generics.ListCreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

    def perform_create(self, serializer):
        parking_lot = get_object_or_404(ParkingLot, pk=self.kwargs["pk"])
        serializer.save(parking_lot=parking_lot)
