# from django.conf.urls import url
from cmath import atan
from webbrowser import get
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .form import Menu, CreateAccount
from .models import Menus, Orders
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from canteensystem.models import CustomUser
import re

@login_required(login_url='login')
def index(request):
    form = Menu()
    datas = Menus.objects.all()

    drinks = Menus.objects.filter(item_categories="drinks")
    addons = Menus.objects.filter(item_categories="addons")
    breakfast = Menus.objects.filter(item_categories="breakfast")
    lunchmeal = Menus.objects.filter(item_categories="lunchmeal")
    
    name = request.user.email
    context = {'form': form, "foods": datas, 'drinks': drinks, 'addons': addons, 'breakfast': breakfast, 'lunchmeal': lunchmeal, 'name': name, 'media_url':settings.MEDIA_URL}
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user.inventory_create or request.user.is_superuser:
                form = Menu(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('index')
            else:
                return redirect('index')
    else:
        form = Menu()

    return render(request, 'index.html', context)


@login_required(login_url='login')
def menu(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.menu_create:
            form = Orders()
            drinks = Menus.objects.filter(item_categories="drinks")
            addons = Menus.objects.filter(item_categories="addons")
            breakfast = Menus.objects.filter(item_categories="breakfast")
            lunchmeals = Menus.objects.filter(item_categories="lunchmeal")
            # getId = Menus.objects.get(id)
            name = request.user.email

            context = {'drinks': drinks, 'addons': addons, 'breakfast': breakfast, 'lunchmeals': lunchmeals, 'name': name, 'media_url':settings.MEDIA_URL}

            if request.method == 'POST':
                foods = []
                for key, values in request.POST.lists():
                    if key == 'foods':
                        foods.append(values)
                    
                print(foods)
                total = request.POST.get("total-purchase")

                for food in foods:
                    form.item = ' '.join(food)
                    form.save()
                    
                form.time = request.POST.get("hour")
                form.item_status = 'PENDING'
                form.total_purchase = total
                form.save()

            return render(request, 'menu.html', context)

        else:
            return redirect('index')    

@login_required(login_url='login')
def inventory(request):
    if request.user.is_authenticated:
        if request.user.orders_delete or request.user.orders_update or request.user.is_superuser:
            name = request.user.email
            order = Orders.objects.all()
            context = {'order': order, 'name': name}
            return render(request, 'inventory.html', context)
        else:
            return redirect('index')

@login_required(login_url='login')
def admins(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.admins_create or request.user.admins_update:
            name = request.user.email
            users = CustomUser.objects.all()        
            print(CustomUser.admins_create)
            context = {'users': users, 'name': name}
            return render(request, 'users.html', context)
        else:
            return redirect('index')

@login_required(login_url='login')
def permission(request, pk):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.admins_update:    
            datas = CustomUser.objects.get(id=pk)
            email = request.user.email
            uemail = datas.email
            name = datas.username
            uid = datas.id
            if request.method == 'POST':
                datas.admins_create = request.POST.get('admins_create')
                datas.admins_update = request.POST.get('admins_update')
                datas.orders_update = request.POST.get('orders_update')
                datas.orders_delete = request.POST.get('orders_delete')
                datas.inventory_create = request.POST.get('inventory_create')
                datas.inventory_update = request.POST.get('inventory_update')
                datas.inventory_delete = request.POST.get('inventory_delete')
                datas.menu_create = request.POST.get('menu_create')
                datas.save()
                return redirect('admin-accounts')

            context = {'datas': datas, 'name': name, 'email':email, 'uid': uid, 'uemail': uemail}

            return render(request, 'permissions.html/', context)

        else:
            return redirect('index')

    else:
        return redirect('index')


@login_required(login_url='login')
def updateFood(request, pk):
    if request.user.is_authenticated:
        if request.user.inventory_update or request.user.is_superuser:
            datas = Menus.objects.get(id=pk)
            form = Menu(instance=datas)
            name = request.user.email
            print("datas: ",datas.item_quantity)


            drinks = Menus.objects.filter(item_categories="drinks")
            addons = Menus.objects.filter(item_categories="addons")
            breakfast = Menus.objects.filter(item_categories="breakfast")
            lunchmeals = Menus.objects.filter(item_categories="lunchmeal")
            if request.method == 'POST':
                form = Menu(request.POST, request.FILES, instance=datas)
                if form.is_valid():
                    form.save()
                    return redirect('index')

            context = {'form': form, 'drinks': drinks, 'addons': addons, 'breakfast': breakfast, 'lunchmeals': lunchmeals, 'name':name, 'media_url':settings.MEDIA_URL}

            return render(request, 'update.html/', context)

        return redirect('index')

@login_required(login_url='login')
def deleteFood(request, pk):
    if request.user.is_authenticated:
        if request.user.inventory_delete or request.user.is_superuser:
            datas = Menus.objects.get(id=pk)
            if request.method == "POST":
                datas.delete() 
                return redirect('index')
        else:
            return redirect('index')

        context = {'item':datas, 'media_url':settings.MEDIA_URL}
        return render(request, 'delete.html/', context)

@login_required(login_url='login')
def cancelOrder(request, pk):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.orders_update:
            datas = Orders.objects.get(id=pk)
            if request.method == "POST":
                datas.item_status = "CANCELLED"
                datas.save()
                return redirect('inventory')
        else:
            return redirect('/orders')

        context = {'item': datas}
        return render(request, 'cancel-order.html/', context)

@login_required(login_url='login')
def approveOrder(request, pk):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.orders_update:
            datas = Orders.objects.get(id=pk)
            if request.method == "POST":
                datas.item_status = "SUCCESS"
                datas.save()
                return redirect('inventory')
        else:
            return redirect('/orders')

        context = {'item': datas}
        return render(request, 'approve-order.html/', context)

@login_required(login_url='login')
def clearInventory(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.orders_delete:
            datas = Orders.objects.all()
            if request.method == "POST":
                datas.delete()
                return redirect('inventory')
        else:
            return redirect('index')

    context = {'item':datas}
    return render(request, 'clear-inventory.html', context)

def loginAccount(request):
    if request.user.is_authenticated:
        return redirect('index')

    else:
        form = CreateAccount()
        if request.method == "POST":
            form = CreateAccount(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password1')

            user = authenticate(request, username=username, password=password)
            
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('index')

            else:
                messages.info(request, "Username or Password is Incorrect.")
        
        context = {'form': form}
        return render(request, 'accounts/login.html', context)


@login_required(login_url='login')
def createAccount(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.admins_create:
            form = CreateAccount()
            if request.method == "POST":
                form = CreateAccount(request.POST)
                fname = request.POST.get('first_name')
                lname = request.POST.get('last_name')
                password = request.POST.get('password1')
                password2 = request.POST.get('password2')
                user = request.POST.get('username')

                min = 8
                regex = re.compile('[.@_!#$%^&*()<>?/\|}{~:]')

                if form.is_valid():
                    if fname == '' or lname == '':
                        messages.info(request, "Fill all forms.")

                    elif regex.search(user) != None or regex.search(fname) != None or regex.search(lname) != None or regex.search(password) != None:
                        messages.info(request, "Symbols and special characters not allowed.")

                    else:
                        form.instance.is_staff = True
                        form.save()

                        return redirect('admin-accounts')

                else:
                    exist = CustomUser.objects.filter(username=user).exists()
                    if fname == '' or lname == '' or password == '' or password2 == '' or user == '':
                        messages.info(request, "Fill all forms.")
                        
                    elif password != password2:
                        messages.info(request, "Password does not match. Please try again.")

                    elif exist:
                        messages.info(request, "Username already exist.")

                    elif len(password) < min:
                        messages.info(request, "Password must be at least 8 characters long.")

                    else:
                        messages.info(request, "Password must have:")
                        messages.info(request, "Lower and uppercase characters.")
                        messages.info(request, "At least single number.")

            context = {'form': form}

            return render(request, 'accounts/registration.html', context)
        else:
            return redirect('index')

def logoutAccount(request):
    logout(request)
    return redirect('login')
