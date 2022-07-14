from django.shortcuts import render
from rest_framework.views import APIView, Response

from .models import Dev


# Create your views here.
class DevsView(APIView):
    def get():
        ...

    def post(self, request):
        dev = Dev.objects.create(**request.data)

        return Response("oi")
