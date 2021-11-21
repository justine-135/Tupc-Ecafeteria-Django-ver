from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import Menu
from .models import Menus, Orders
from django.conf import settings


def index(request):
    form = Menu()
    datas = Menus.objects.all()

    drinks = Menus.objects.filter(item_categories="drinks")
    addons = Menus.objects.filter(item_categories="addons")
    breakfast = Menus.objects.filter(item_categories="breakfast")
    lunchmeal = Menus.objects.filter(item_categories="lunchmeal")
    

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
    form = Orders()
    drinks = Menus.objects.filter(item_categories="drinks")
    addons = Menus.objects.filter(item_categories="addons")
    breakfast = Menus.objects.filter(item_categories="breakfast")
    lunchmeals = Menus.objects.filter(item_categories="lunchmeal")
    context = {'drinks': drinks, 'addons': addons, 'breakfast': breakfast, 'lunchmeals': lunchmeals, 'media_url':settings.MEDIA_URL}

    
    if request.method == 'POST':
        # sample = request.POST.get("foods")
        # sample1 = request.POST.get("prices")
        # sample3 = request.POST.get("quantities")
        foods = []
        prices = []

        for key, values in request.POST.lists():
            if key == 'foods':
                foods.append(values)
        total = request.POST.get("total-purchase")

        print(foods)
        for food in foods:
            
            form.item = ' '.join(food)
            form.save()
        form.time = request.POST.get("hour")
        form.item_status = 'SUCCESS'
        form.total_purchase = total
        form.save()


    
    return render(request, 'menu.html', context)


def inventory(request):
    order = Orders.objects.filter(item_status="SUCCESS")
    context = {'order': order}
    return render(request, 'inventory.html', context)
