from django.urls import path
from rest_framework import authtoken
from rest_framework.authtoken import views as authview

from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view()),
    path("login/", authtoken.views.obtain_auth_token),
    # path("login/", authview.obtain_auth_token),
]
