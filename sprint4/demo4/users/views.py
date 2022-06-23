import ipdb
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404, render
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

# from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response, status

from users.models import User
from users.permissions import IsLucira, IsOwnerOrReadOnly
from users.serializers import LoginSerializer, RegisterSerializer


class ProtectedView(APIView):
    # Define qual o tipo de authenticação
    authentication_classes = [TokenAuthentication]
    # Define quais as regras de permissão
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"msg": "bem vindo a rota GET"})

    def post(self, request):
        return Response({"msg": "bem vindo a rota POST"}, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated, IsLucira]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)

        serializer = RegisterSerializer(user)

        return Response(serializer.data)

    def patch(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)

        self.check_object_permissions(request, user)

        serializer = RegisterSerializer(user, request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        # user = User.objects.create_superuser(**serializer.validated_data)

        # serializer = RegisterSerializer(user)

        return Response(serializer.data, status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            # token = Token.objects.get_or_create(user=user)[0]

            return Response({"token": token.key})

        return Response(
            {"detail": "invalid email or password"}, status.HTTP_401_UNAUTHORIZED
        )
