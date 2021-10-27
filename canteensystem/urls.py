from django.urls import path

from . import views

urlpatterns = [
    # map views to urls
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('inventory', views.inventory, name='inventory'),
]
