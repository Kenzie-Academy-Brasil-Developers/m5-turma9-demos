from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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
    # serializer_class é um atributo obrigatório, a não ser que voce sobrescreva get_serializer_class
    # serializer_class = DetailParkingLotSerializer

    # Utilizando o SerializerByMethodMixin, sobrescrevemos da mesma forma o get_serializer_class
    # que poderiamos ter sobrescrito aqui na view, mas consiguimos reaproveita-lo em outras views
    # def get_serializer_class(self, *args, **kwargs):
    #     return self.serializer_map.get(self.request.method, self.serializer_class)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RetrieveUpdateDestroyParkingLotView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = ParkingLot.objects.all()
    serializer_class = ListParkingLotSerializer
