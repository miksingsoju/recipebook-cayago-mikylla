# app/admin.py
from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

# registering the model and the admin is what tells
# Django that admin pages must be generated for the models specified
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "author"

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
