from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status

from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    # Poderia fazer tudo numa unica view
    def patch(self, request, user_id):
        ...

    def put(self, request, user_id):
        ...

    def get(self, request, user_id=None):
        # if user_id:
        #     try:
        #         user = User.objects.get(pk=user_id)
        #     except User.DoesNotExist:
        #         return Response(
        #             {"error": "usuário não existe"}, status.HTTP_404_NOT_FOUND
        #         )

        #     serializer = UserSerializer(user)

        #     return Response(serializer.data)

        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request):
        # print(request.data) -> dicionario

        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        # if not serializer.is_valid():
        #     # return Response(serializer.errors, 400)
        #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        # user = User(**serializer.validated_data)
        # user.save()

        # serializer = UserSerializer(user)

        # .save() chama o create() do UserSerializer
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserViewDetail(APIView):
    def get(self, request, user_id):
        # try:
        #     user = User.objects.get(pk=user_id)
        # except User.DoesNotExist:
        #     return Response({"error": "usuário não existe"}, status.HTTP_404_NOT_FOUND)

        # serializer = UserSerializer(user)

        # return Response(serializer.data)

        user = get_object_or_404(User, pk=user_id)

        serializer = UserSerializer(user)

        return Response(serializer.data)

    def delete(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)

        serializer = UserSerializer(user, request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
        except KeyError:
            return Response(
                {"error": "não pode atualizar endereço"}, status.HTTP_400_BAD_REQUEST
            )

        return Response(serializer.data)
