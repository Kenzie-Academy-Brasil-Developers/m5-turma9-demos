from django.shortcuts import get_object_or_404, render
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView, Response, status

from books.models import Book
from books.permissions import IsOwnerOrReadOnly

from .serializers import BookSerializer


class BookView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(owner=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):
        books = Book.objects.all()

        result_page = self.paginate_queryset(books, request, self)
        serializer = BookSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


class BookDetailsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def patch(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)

        self.check_object_permissions(request, book)

        serializer = BookSerializer(book, request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)
