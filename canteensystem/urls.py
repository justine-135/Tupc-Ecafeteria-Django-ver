from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('canteensystem/kamusta', views.hello, name="kamusta"),

]
