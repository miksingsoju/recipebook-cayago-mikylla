from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required


# Create your views here.
def custom_login(request):
    return render(request, 'registration/login.html')


@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes':recipes
    }
    return render(request,'recipe_list.html',ctx)

@login_required
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


