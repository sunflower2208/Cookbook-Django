from django.db import models

# Create your models here.
class RecipeName(models.Model):
    name = models.CharField(max_length=200)
    steps = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=200)
    quantity = models.FloatField()
    quantity_unit = models.CharField(max_length=10)
    recipes = models.ForeignKey(RecipeName, on_delete=models.CASCADE)

    class Meta:
        ordering = ['ingredient_name']

    def __str__(self):
        return self.ingredient_name