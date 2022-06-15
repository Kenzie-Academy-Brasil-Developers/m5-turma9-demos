from rest_framework.views import APIView, Response, status

from .models import User
from .serializers import UserSerializer


# Create your views here.
class UserView(APIView):
    def get(self, _):
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
