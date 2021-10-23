from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # render index.html using render function
    return render(request, 'index.html')
