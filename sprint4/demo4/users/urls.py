from django.urls import path

# from .views import LoginView, RegisterView
from . import views

urlpatterns = [
    path("users/register/", views.RegisterView.as_view()),
    path("users/login/", views.LoginView.as_view()),
    path("users/protected/", views.ProtectedView.as_view()),
    path("users/<int:user_id>/", views.UserDetailView.as_view()),
]
