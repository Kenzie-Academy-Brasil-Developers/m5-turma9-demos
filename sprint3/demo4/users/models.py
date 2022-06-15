from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, unique=True)

    def __repr__(self):
        return f"User {self.id} - {self.email}"
