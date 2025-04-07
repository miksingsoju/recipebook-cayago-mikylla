from django import forms
from .models import Recipe, RecipeIngredient, RecipeImage, Ingredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']
        
class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity','recipe']

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']