from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # render index.html using render function
    return render(request, 'index.html')

def menu(request):
    # render menu.html using render function
    return render(request, 'menu.html')

def inventory(request):
    # render inventory.html using render function
    return render(request, 'inventory.html')

