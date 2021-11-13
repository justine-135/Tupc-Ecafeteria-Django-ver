from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import BreakfastForm


def index(request):
    # render index.html using render function
    form = BreakfastForm()
    # lform = LunchmealForm(request)
    # dform = DrinksForm(request)
    # aform = AddonsForm(request)
    # context = {'breakfast_form': form, 'lunchmeal_form': lform,
    #            'drinks_form': dform, 'addons_form': aform}
 
    if request.method == 'POST':
        form = BreakfastForm(request.POST)
        print('post')
        if form.is_valid():
            print('hi')

            form.save()
            return redirect('index')

    else:
        print('faled')
        form = BreakfastForm()

        # return redirect('index')
    # elif lform.is_valid():
    #     lform.save()
    # elif dform.is_valid():
    #     dform.save()
    # elif aform.is_valid():
    #     aform.save()
    context = {'form': form}

    return render(request, 'index.html', context)


def menu(request):
    # render menu.html using render function
    return render(request, 'menu.html')


def inventory(request):
    # render inventory.html using render function
    return render(request, 'inventory.html')
