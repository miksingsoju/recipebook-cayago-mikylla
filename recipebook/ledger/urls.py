from django.urls import path
from .views import index, recipe_list

urlpatterns = [
path('', index, name='index'),
path('recipe/list', recipe_list, name='recipe list'),

]
# This might be needed, depending
app_name = "ledger"