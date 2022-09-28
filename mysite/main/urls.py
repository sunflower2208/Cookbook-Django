from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("<int:id>/", views.index, name="index"),
    path("create/", views.create_recipe, name="create"),
    path("add_ing/<int:id>/", views.add_ingredients, name="add_ing"),
    path("view/", views.view, name='view'),
    path("random/", views.random, name='random'),
    path("search/", views.searcher, name="searcher"),
]