from django.shortcuts import render
from .models import Recipe, RecipeIngredient, User
from django.contrib.auth.decorators import login_required


@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes':recipes
    }
    return render(request,'recipe_list.html',ctx)

@login_required
def recipe_detail(request,num=1):
    recipe = Recipe.objects.get(pk=num)
    ctx = {
            "recipe": recipe,
        }
    return render(request,'recipe.html',ctx)


