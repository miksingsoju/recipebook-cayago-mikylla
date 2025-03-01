from django.urls import path
from .views import recipe_list, recipe
urlpatterns = [
path('', recipe_list, name='recipe list'),
path('recipes/list', recipe_list, name='recipe list'),
path('recipe/<int:num>', recipe, name='recipe'),
]
# This might be needed, depending
app_name = "ledger"