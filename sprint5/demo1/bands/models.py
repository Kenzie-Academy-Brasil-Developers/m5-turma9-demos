from django.db import models


# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=127)
    year_formed = models.DateField(null=True, blank=True, default=None)
