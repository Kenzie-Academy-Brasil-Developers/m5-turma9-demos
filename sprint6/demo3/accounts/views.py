from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView, Response, status

from .models import Account
from .serializers import AccountSerializer


class RegisterView(APIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def post(self, request):
        serializer = AccountSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
