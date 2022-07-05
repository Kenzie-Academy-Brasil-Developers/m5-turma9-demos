from django.shortcuts import get_object_or_404, render
from floors.models import Floor, Spot
from parking_lots.models import ParkingLot
from rest_framework import generics
from rest_framework.views import Response, status

from vehicle.models import Vehicle
from vehicle.serializers import VehicleSerializer


# Create your views here.
class ListCreateVehicleView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def perform_create(self, serializer):
        import ipdb

        vehicle_type = serializer.validated_data["vehicle_type"]

        # ipdb.set_trace()
        # Problema do floor não estar ligado ao parking_lot
        pl = get_object_or_404(ParkingLot, pk=self.kwargs["pl_id"])

        # TODO:
        # Floor que não existe no PL está sendo reconhecido pelo POST
        # Response não consegue ser lido pelo perform_create
        try:
            # ipdb.set_trace()
            floor = pl.floors.get(id=self.kwargs["floor_id"])
            print()
        except Floor.DoesNotExist:
            return Response({"detail": "floor not found"}, status.HTTP_404_NOT_FOUND)
        # floor = get_object_or_404(Floor, pk=self.kwargs["floor_id"])

        floor = pl.floors.filter(id=self.kwargs["floor_id"]).first()

        if not floor:
            return Response({"detail": "floor not found"}, status.HTTP_404_NOT_FOUND)
        spot_found = floor.find_spot_for_vehicle_type(vehicle_type)

        if not spot_found:
            return Response(
                {
                    "detail": f"floor {floor.name} has no available spots for {vehicle_type}"
                },
                status.HTTP_409_CONFLICT,
            )

        serializer.save(spot=spot_found)
