from django.contrib.auth.models import AbstractUser
from django.db import models

from users.utils import CustomUserManager


# Create your models here.
class User(AbstractUser):
    # Modificando nome de tabela
    # class Meta:
    #     db_table = "meu_nome_de_tabela"

    email = models.EmailField(max_length=255, unique=True)
    age = models.IntegerField()

    username = None

    REQUIRED_FIELDS = ["age"]
    USERNAME_FIELD = "email"
    objects = CustomUserManager()
