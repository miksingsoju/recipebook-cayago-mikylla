from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader
from .models import Recipe

# Create your views here.
def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes':recipes
    }
    return render(request,'recipe_list.html',ctx)

def recipe_detail(request,num=1):
    if num == 1:
        recipe = Recipe.objects.get(name="Recipe 1")
        ctx = {
            "recipe": recipe
        }

    elif num == 2:
        recipe = Recipe.objects.get(name="Recipe 2")
        ctx = {
            "recipe": recipe
        }
    return render(request,'recipe.html',{"recipe":recipe})


