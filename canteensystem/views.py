from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import BreakfastForm


def index(request):
    # render index.html using render function
    form = BreakfastForm()
    context = {'form': form}
 
    if request.method == 'POST':
        form = BreakfastForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BreakfastForm()

    return render(request, 'index.html', context)


def menu(request):
    # render menu.html using render function
    return render(request, 'menu.html')


def inventory(request):
    # render inventory.html using render function
    return render(request, 'inventory.html')
