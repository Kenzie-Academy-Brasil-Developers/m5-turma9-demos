from rest_framework import serializers
from users.serializers import RegisterSerializer

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    owner = RegisterSerializer()

    class Meta:
        model = Book
        # fields = ["name", "published_date", "status"]
        fields = "__all__"
        # exclude = ["owner"]
        read_only_fields = ["id", "owner"]
