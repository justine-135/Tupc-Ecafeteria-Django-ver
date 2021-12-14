from django.conf.urls import url
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .form import Menu, CreateAccount
from .models import Menus, Orders
from django.conf import settings

@login_required(login_url='login')
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

@login_required(login_url='login')
def inventory(request):
    order = Orders.objects.all()
    context = {'order': order}
    return render(request, 'inventory.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteFood(request, pk):
    datas = Menus.objects.get(id=pk)
    if request.method == "POST":
        datas.delete() 
        return redirect('index')

    context = {'item':datas, 'media_url':settings.MEDIA_URL}
    return render(request, 'delete.html/', context)

@login_required(login_url='login')
def cancelOrder(request, pk):
    datas = Orders.objects.get(id=pk)
    if request.method == "POST":
        datas.item_status = "CANCELLED"
        datas.save()
        print(datas)
        return redirect('inventory')
    context = {'item': datas}

    return render(request, 'cancel-order.html/', context)

@login_required(login_url='login')
def clearInventory(request):
    datas = Orders.objects.all()
    if request.method == "POST":
        datas.delete()
        return redirect('inventory')

    print(datas)
    context = {'item':datas}

    return render(request, 'clear-inventory.html', context)

def loginAccount(request):
    form = CreateAccount()
    if request.method == "POST":
        form = CreateAccount(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Username or Password is Incorrect.")
    
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def createAccount(request):
    form = CreateAccount()

    if request.method == "POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered Successfully')
            return redirect('login')
        else:
            messages.info(request, "Password does not match. Please try again.")

    context = {'form': form}

    return render(request, 'accounts/registration.html', context)

def logoutAccount(request):
    logout(request)
    return redirect('login')
