from django.contrib.auth import authenticate
from django.core.checks import messages
from django.shortcuts import render, redirect
from .form import Menu, CreateAccount
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

    return render(request, 'index.html', context)

def menu(request):
    form = Orders()
    drinks = Menus.objects.filter(item_categories="drinks")
    addons = Menus.objects.filter(item_categories="addons")
    breakfast = Menus.objects.filter(item_categories="breakfast")
    lunchmeals = Menus.objects.filter(item_categories="lunchmeal")
    context = {'drinks': drinks, 'addons': addons, 'breakfast': breakfast, 'lunchmeals': lunchmeals, 'media_url':settings.MEDIA_URL}

    
    if request.method == 'POST':
        foods = []

        for key, values in request.POST.lists():
            if key == 'foods':
                foods.append(values)
        total = request.POST.get("total-purchase")

        for food in foods:
            form.item = ' '.join(food)
            form.save()
            
        form.time = request.POST.get("hour")
        form.item_status = 'SUCCESS'
        form.total_purchase = total
        form.save()


    
    return render(request, 'menu.html', context)


def inventory(request):
    order = Orders.objects.all()
    context = {'order': order}
    return render(request, 'inventory.html', context)

def updateFood(request, pk):
    datas = Menus.objects.get(id=pk)
    form = Menu(instance=datas)
    drinks = Menus.objects.filter(item_categories="drinks")
    addons = Menus.objects.filter(item_categories="addons")
    breakfast = Menus.objects.filter(item_categories="breakfast")
    lunchmeals = Menus.objects.filter(item_categories="lunchmeal")
    if request.method == 'POST':
        form = Menu(request.POST, request.FILES, instance=datas)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, 'drinks': drinks, 'addons': addons, 'breakfast': breakfast, 'lunchmeals': lunchmeals, 'media_url':settings.MEDIA_URL}

    return render(request, 'update.html/', context)


def deleteFood(request, pk):
    datas = Menus.objects.get(id=pk)
    if request.method == "POST":
        datas.delete() 
        return redirect('index')

    context = {'item':datas, 'media_url':settings.MEDIA_URL}
    return render(request, 'delete.html/', context)

def cancelOrder(request, pk):
    datas = Orders.objects.get(id=pk)
    if request.method == "POST":
        datas.item_status = "CANCELLED"
        datas.save()
        print(datas)
        return redirect('inventory')
    context = {'item': datas}

    return render(request, 'cancel-order.html/', context)

def clearInventory(request):
    datas = Orders.objects.all()
    if request.method == "POST":
        datas.delete()
        return redirect('inventory')

    print(datas)
    context = {'item':datas}

    return render(request, 'clear-inventory.html', context)

def login(request):
    form = login()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('registration')
        else:
            messages.info(request, "Invalid Credentials. user Not Found")
    
    context = {}
    return render(request, 'accounts/login.html', context)

def createAccount(request):
    form = CreateAccount()
    if request.method == "POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            form.save
        return redirect('login')

    context = {'form': form}

    return render(request, 'accounts/registration.html', context)

def logout(request):
    logout(request)
    return redirect('login')
