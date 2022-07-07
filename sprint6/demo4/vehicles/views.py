from django.http import Http404
from django.shortcuts import get_object_or_404, render
from floors.models import Floor, Spot
from parking_lots.models import ParkingLot
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.views import Response, status

from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer

from .exceptions import NoSpotAvailableError


# Create your views here.
class ListCreateVehicleView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def perform_create(self, serializer):
        vehicle_type = serializer.validated_data["vehicle_type"]

        floor = get_object_or_404(
            Floor, pk=self.kwargs["floor_id"], parking_lot=self.kwargs["pl_id"]
        )

        spot_found = floor.find_spot_for_vehicle_type(vehicle_type)

        if not spot_found:
            raise NoSpotAvailableError

        serializer.save(spot=spot_found)


class UpdateVehicleView(generics.UpdateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_object(self) -> Vehicle:
        floor = get_object_or_404(
            Floor, pk=self.kwargs["floor_id"], parking_lot=self.kwargs["pl_id"]
        )

        # filter sempre retorna um queryset
        spot_found = floor.spots.filter(vehicle__id=self.kwargs["vehicle_id"]).first()

        if not spot_found:
            raise NoSpotAvailableError

        vehicle: Vehicle = spot_found.vehicle

        vehicle.calculate_payment()

        return vehicle
