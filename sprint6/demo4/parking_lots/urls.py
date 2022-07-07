from django.urls import path
from floors.views import ListCreateFloor
from vehicles.views import ListCreateVehicleView, UpdateVehicleView

from . import views

urlpatterns = [
    path("parking-lots/", views.ListCreateParkingLotView.as_view()),
    path("parking-lots/<pk>/", views.RetrieveUpdateDestroyParkingLotView.as_view()),
    path("parking-lots/<pk>/floors/", ListCreateFloor.as_view()),
    path(
        "parking-lots/<pl_id>/floors/<floor_id>/vehicles/",
        ListCreateVehicleView.as_view(),
    ),
    path(
        "parking-lots/<pl_id>/floors/<floor_id>/vehicles/<int:vehicle_id>/",
        UpdateVehicleView.as_view(),
    ),
]
