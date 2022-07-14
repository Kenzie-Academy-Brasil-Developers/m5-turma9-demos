from django.db import models


# Create your models here.
class Dev(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField()
