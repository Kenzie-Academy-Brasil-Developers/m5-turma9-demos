from django.shortcuts import render
from rest_framework.views import APIView, Response, status

from books.models import Book

from .serializers import BookSerializer


# Create your views here.
class BookView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)
