from django.shortcuts import render, redirect
from .models import Recipe, RecipeImage
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, RecipeIngredientForm, IngredientForm
from .forms import RecipeImageForm

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
    images = RecipeImage.objects.filter(recipe__exact=recipe)
    ctx = {
            "recipe": recipe,
            "images": images,
        }
    return render(request,'recipe.html',ctx)

@login_required
def add_recipe(request):
    recipe_form = RecipeForm()
    ingredient_form = IngredientForm()
    recipe_ingredient_form = RecipeIngredientForm()

    if request.method == 'POST':
        if 'recipe_submit' in request.POST:
            recipe_form = RecipeForm(request.POST)
            if recipe_form.is_valid():
                recipe = recipe_form.save(commit=False)
                recipe.author = request.user.profile
                recipe.save()
                return redirect(recipe,pk=recipe.pk)

        elif 'ingredient_submit' in request.POST:
            ingredient_form = IngredientForm(request.POST)
            if ingredient_form.is_valid():
                ingredient_form.save()
                return redirect('ledger:add_recipe')

        elif 'recipe_ingredient_submit' in request.POST:
            recipe_ingredient_form = RecipeIngredientForm(request.POST)
            if recipe_ingredient_form.is_valid():
                recipe_ingredient_form.save()
                return redirect('ledger:add_recipe')


    return render(request, 'ledger/add_recipe.html', {
        'recipe_form': recipe_form,
        'ingredient_form': ingredient_form,
        'recipe_ingredient_form': recipe_ingredient_form
    })

def add_image(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.recipe = recipe
            new_image.save()
            return redirect(recipe, pk=recipe.pk)
    else:
        form = RecipeImageForm()

    return render(request, 'ledger/add_image.html', {'form': form, 'recipe': recipe})