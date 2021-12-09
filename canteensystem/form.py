from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField


class Menu(forms.ModelForm):
    class Meta:
        model = Menus
        fields = [ 'item_categories', 'item_name', 'item_price', 'item_quantity', 'item_img',]
        widgets = {'item_categories': forms.Select(attrs={'id': 'dropdown'}),
            'item_name': forms.TextInput(attrs={'placeholder': 'Enter food', 'onkeypress': 'return (event.charCode > 64 && event.charCode < 91) || (event.charCode > 96 && event.charCode < 123) || (event.charCode==32)', 'onpaste':"return false", 'ondrag':"return false", 'ondrop':"return false"}),
        'item_price': forms.TextInput(attrs={'placeholder': 'Enter Price', 'type': 'number', 'onkeypress': 'return event.keyCode === 8 || event.charCode >= 48 && event.charCode <= 57', 'onpaste':"return false", 'ondrag':"return false", 'ondrop':"return false"}),
        'item_quantity': forms.TextInput(attrs={'placeholder': 'Enter Quantity', 'type': 'number', 'onkeypress': 'return event.keyCode === 8 || event.charCode >= 48 && event.charCode <= 57', 'onpaste':"return false", 'ondrag':"return false", 'ondrop':"return false"})}

class CreateAccount(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
