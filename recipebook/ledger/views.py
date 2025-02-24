from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('recipe_list.html')
    return HttpResponse(template.render())
def recipe_list(request):
    template = loader.get_template('recipe_list.html')
    return HttpResponse(template.render())

