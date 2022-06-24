from rest_framework import serializers
from users.serializers import RegisterSerializer

from books.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    owner = RegisterSerializer(read_only=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ["id"]

    def update(self, instance: Book, validated_data: dict):
        authors = validated_data.pop("authors", None)

        # lista de objetos author
        if authors:
            author_list = []
            for author in authors:
                author, _ = Author.objects.get_or_create(**author)
                author_list.append(author)

            # Vai resetar os authors e criar os novos
            instance.authors.set(author_list)
            # Vai adicionar mais authors, mantendo os que existiam
            # instance.authors.add(*author_list)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    # def create(self, validated_data: dict) -> Book:
    #     # validated_data['owner']

    #     return Book.objects.create(**validated_data)
