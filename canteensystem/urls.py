from django.urls import path

from . import views

urlpatterns = [
    # read views.py and execute index function
    path('', views.index, name='index'),

]
