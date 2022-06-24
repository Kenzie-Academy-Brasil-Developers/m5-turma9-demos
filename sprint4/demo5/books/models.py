from django.db import models


class BookStatus(models.TextChoices):
    OLD = ("old",)
    NEW = ("new",)
    DEFAULT = ("not informed",)


# Create your models here.
class Book(models.Model):
    # class Meta:
    #     db_table = "novo_nome"

    name = models.CharField(max_length=255)
    published_date = models.DateField()

    status = models.CharField(
        max_length=50, choices=BookStatus.choices, default=BookStatus.DEFAULT
    )

    # 1 -> N : User Books
    owner = models.ForeignKey(
        "users.User", related_name="books", on_delete=models.CASCADE
    )

    authors = models.ManyToManyField("books.Author", related_name="books")

    def __str__(self):
        return f"{self.id} - {self.name}"


class Author(models.Model):
    name = models.CharField(max_length=255)
