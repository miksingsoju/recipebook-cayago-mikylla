from django.urls import path
from .views import recipe_list, recipe_detail
urlpatterns = [
path('', recipe_list, name='recipe-list'),
path('recipes/list', recipe_list, name='recipe-list'),
path('recipe/<int:num>/', recipe_detail,name='recipe-detail'),
]
# This might be needed, depending
app_name = "ledger"