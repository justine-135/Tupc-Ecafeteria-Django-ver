from django.urls import path

from . import views

urlpatterns = [
    # read views.py and execute index function
    # read views.py and execute menu function
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),

]
