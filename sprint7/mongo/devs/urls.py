from django.urls import path

from . import views

urlpatterns = [
    path("devs/", views.DevsView.as_view()),
]
