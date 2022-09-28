from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import RecipeName, Ingredient
from .forms import RecipeForm, IngredientForm
from random import choice

# Create your views here.
def index(response, id):
    r = RecipeName.objects.get(id=id)
    return render(response, "main/recipe.html", {"r":r})


def home(response):
    return render(response, "main/home.html", {})


def create_recipe(response):
    if response.method == "POST":
        form = RecipeForm(response.POST)

        if form.is_valid():
            r = form.save()
            return HttpResponseRedirect("/add_ing/%i" %r.id)

    else:
        form = RecipeForm()

    return render(response, "main/create.html", {"form": form})


def add_ingredients(response,id):
    r = RecipeName.objects.get(id=id)
    if response.method == 'POST':

        if response.POST.get("save"):
            return HttpResponseRedirect("/%i" %r.id)

        elif response.POST.get("newItem"):
            form = IngredientForm(response.POST)
            if form.is_valid():
                i = form.save(commit=False)
                i.recipes = r
                i.save()
                form = IngredientForm()

    else:
        form = IngredientForm()

    return render(response, "main/add_ing.html", {"r": r, "form": form})


def view(response):
    recipes = RecipeName.objects.all()
    return render(response, "main/view.html", {"recipes": recipes})


def random(response):
    recipes = RecipeName.objects.all()
    r = choice(recipes)
    return HttpResponseRedirect("/%i" %r.id)


def searcher(response):
    if response.method == 'POST':
        searched = response.POST.get('searcher')
        items_r = RecipeName.objects.filter(name__contains=searched)
        items_i = Ingredient.objects.filter(ingredient_name__contains=searched)
        return render(response, "main/searcher.html", {"searched": searched, "items_r": items_r, "items_i": items_i})
    else:
        return render(response, "main/searcher.html", {})