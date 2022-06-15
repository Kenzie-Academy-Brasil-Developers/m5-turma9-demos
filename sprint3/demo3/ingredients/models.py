from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=40)

    recipes = models.ManyToManyField("recipes.Recipe", related_name="ingredients")

    def __repr__(self):
        return f"{self.id} - {self.name}"
