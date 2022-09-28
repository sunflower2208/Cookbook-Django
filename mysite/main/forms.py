from django import forms
from .models import RecipeName, Ingredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeName
        fields = ["name", "steps"]

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "steps": forms.Textarea(attrs={'class': 'form-control'}),
        }


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["ingredient_name", "quantity", "quantity_unit"]

        widgets = {
            "ingredient_name": forms.TextInput(attrs={'class': 'form-control'}),
            "quantity": forms.TextInput(attrs={'class': 'form-control'}),
            "quantity_unit": forms.TextInput(attrs={'class': 'form-control'}),
        }
