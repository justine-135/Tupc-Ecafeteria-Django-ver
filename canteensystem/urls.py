from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    # map views to urls
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('orders/', views.inventory, name='inventory'),
    path('admin-accounts/', views.admins, name='admin-accounts'),
    path('permissions/<str:pk>', views.permission, name='permissions'),
    path('update/<str:pk>/', views.updateFood, name='update'),
    path('delete/<str:pk>/', views.deleteFood, name='delete'),
    path('cancel/<str:pk>/', views.cancelOrder, name='cancel-order'),
    path('clear-inventory/', views.clearInventory, name='clear-inventory'),
    path('registration/', views.createAccount, name ='registration'),
    path('login/', views.loginAccount, name ='login'),
    path('logout/', views.logoutAccount, name ='logout'),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
