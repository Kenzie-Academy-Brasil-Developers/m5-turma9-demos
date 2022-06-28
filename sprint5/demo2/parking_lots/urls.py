from django.urls import path

from . import views

urlpatterns = [
    path("parking-lots/", views.ListCreateParkingLotView.as_view()),
    path("parking-lots/<pk>/", views.RetrieveUpdateDestroyParkingLotView.as_view()),
]
