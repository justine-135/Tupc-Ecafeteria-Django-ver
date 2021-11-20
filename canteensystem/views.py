from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import Menu
from .models import Menus
from django.conf import settings


def index(request):
    form = Menu()
    datas = Menus.objects.all()

    #filter menu
    drinks = Menus.objects.filter(item_categories="drinks")
    addons = Menus.objects.filter(item_categories="addons")
    breakfast = Menus.objects.filter(item_categories="breakfast")
    lunchmeal = Menus.objects.filter(item_categories="lunchmeal")

    #add filtered here
    context = {'form': form, "foods": datas, 'drinks': drinks, 'addons': addons, 'breakfast': breakfast, 'lunchmeal': lunchmeal, 'media_url':settings.MEDIA_URL}
    if request.method == 'POST':
        form = Menu(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Menu()

    print(addons)
    return render(request, 'index.html', context)


def menu(request):
    drinks = Menus.objects.filter(item_categories="drinks")
    addons = Menus.objects.filter(item_categories="addons")
    breakfast = Menus.objects.filter(item_categories="breakfast")
    lunchmeals = Menus.objects.filter(item_categories="lunchmeal")
    context = {'drinks': drinks, 'addons': addons, 'breakfast': breakfast, 'lunchmeals': lunchmeals, 'media_url':settings.MEDIA_URL}
    if request.method == 'POST':
        print('save')
    else:
        form = Menu()
    
    return render(request, 'menu.html', context)


def inventory(request):
    return render(request, 'inventory.html')
