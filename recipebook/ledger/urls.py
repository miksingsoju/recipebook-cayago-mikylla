from django.urls import path
from .views import recipe_list, recipe_detail, custom_login
urlpatterns = [
path('', custom_login, name='login'),
path('recipes/list', recipe_list, name='recipe-list'),
path('recipe/<int:num>/', recipe_detail,name='recipe-detail'),
]
# This might be needed, depending
app_name = "ledger"