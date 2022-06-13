from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    birthdate = models.DateField(null=True)
    married = models.BooleanField(null=True, blank=True)
    account_balance = models.DecimalField(max_digits=12, decimal_places=2)
    # cents
    # account_balance = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    # last_modified
    updated_at = models.DateTimeField(auto_now=True)
