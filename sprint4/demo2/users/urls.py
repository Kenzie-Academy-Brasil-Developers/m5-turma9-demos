from django.urls import path

from .views import LoginView, RegisterView

urlpatterns = [
    path("users/register/", RegisterView.as_view()),
    path("users/login/", LoginView.as_view()),
]
