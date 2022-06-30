from django.shortcuts import get_object_or_404, render
from parking_lots.models import ParkingLot
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from floors.serializers import FloorSerializer

from .models import Floor
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class ListCreateFloor(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

    def perform_create(self, serializer):
        # import ipdb

        # ipdb.set_trace()
        parking_lot = get_object_or_404(ParkingLot, pk=self.kwargs["pk"])
        serializer.save(parking_lot=parking_lot)
