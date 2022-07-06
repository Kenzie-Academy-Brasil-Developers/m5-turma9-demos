from django.http import Http404
from django.shortcuts import get_object_or_404, render
from floors.models import Floor, Spot
from parking_lots.models import ParkingLot
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.views import Response, status

from vehicle.models import Vehicle
from vehicle.serializers import VehicleSerializer

from .exceptions import NoSpotAvailableError


# Create your views here.
class ListCreateVehicleView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def perform_create(self, serializer):
        vehicle_type = serializer.validated_data["vehicle_type"]

        # pl = get_object_or_404(ParkingLot, pk=self.kwargs["pl_id"])
        floor = get_object_or_404(
            Floor, pk=self.kwargs["floor_id"], parking_lot=self.kwargs["pl_id"]
        )

        # import ipdb

        # ipdb.set_trace()

        # try:
        #     floor = pl.floors.get(id=self.kwargs["floor_id"])
        # except Floor.DoesNotExist:
        #     # raise Http404
        #     raise NotFound("floor not found.")

        spot_found = floor.find_spot_for_vehicle_type(vehicle_type)

        if not spot_found:
            raise NoSpotAvailableError

        serializer.save(spot=spot_found)
