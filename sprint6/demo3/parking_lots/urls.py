from django.urls import path
from floors.views import ListCreateFloor
from vehicle.views import ListCreateVehicleView

from . import views

urlpatterns = [
    path("parking-lots/", views.ListCreateParkingLotView.as_view()),
    path("parking-lots/<pk>/", views.RetrieveUpdateDestroyParkingLotView.as_view()),
    path("parking-lots/<pk>/floors/", ListCreateFloor.as_view()),
    path(
        "parking-lots/<pl_id>/floors/<floor_id>/vehicles/",
        ListCreateVehicleView.as_view(),
    ),
]
