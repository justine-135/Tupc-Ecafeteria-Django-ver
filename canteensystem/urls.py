from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # map views to urls
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('inventory', views.inventory, name='inventory'),
    path('/<str:pk>', views.updateFood, name='update'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
