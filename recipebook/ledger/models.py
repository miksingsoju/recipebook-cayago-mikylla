from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=255)
    
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.name)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    # Made the foreignKey accept NULL and Blank so that django would not have a seizure when I made the migrations
    author = models.ForeignKey(
        Profile, 
        on_delete=models.SET_NULL, 
        blank=True, null=True, 
        related_name='created_recipe')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.id])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients"
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe"
    )

    def __str__(self):
        return self.quantity + ' of ' + self.ingredient.name + ' in ' + self.recipe.name

class RecipeImage(models.Model):
    image = models.ImageField(upload_to='recipe_images/', null=False)
    description = models.TextField(max_length=255)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="recipe_image"
    )
