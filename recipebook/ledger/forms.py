from django import forms
from .models import Recipe, RecipeIngredient, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']