from django.urls import path
from .views import recipe_list, recipe_detail, add_recipe, add_image
urlpatterns = [
    path('', recipe_list, name='recipe-list'),
    path('recipes/list/', recipe_list, name='recipe-list'),
    path('recipe/<int:num>/', recipe_detail,name='recipe-detail'),
    path('recipe/add/', add_recipe, name='add_recipe'),
    path('recipe/<int:pk>/add_image/', add_image, name='add_image'),
]
# This might be needed, depending
app_name = "ledger"