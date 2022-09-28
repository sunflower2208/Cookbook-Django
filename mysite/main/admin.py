from django.contrib import admin
from .models import RecipeName, Ingredient

# Register your models here.
admin.site.register(RecipeName)
admin.site.register(Ingredient)

