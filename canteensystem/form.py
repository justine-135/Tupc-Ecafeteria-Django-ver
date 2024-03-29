from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class Menu(forms.ModelForm):
    class Meta:
        model = Menus
        fields = [ 'item_categories', 'item_name', 'item_price', 'item_quantity', 'item_img',]
        widgets = {'item_categories': forms.Select(attrs={'id': 'dropdown'}),
            'item_name': forms.TextInput(attrs={'placeholder': 'Enter food', 'onkeypress': 'return (event.charCode > 64 && event.charCode < 91) || (event.charCode > 96 && event.charCode < 123) || (event.charCode==32)', 'onpaste':"return false", 'ondrag':"return false", 'ondrop':"return false"}),
        'item_price': forms.TextInput(attrs={'placeholder': 'Enter Price', 'type': 'number', 'onkeypress': 'return event.keyCode === 8 || event.charCode >= 48 && event.charCode <= 57', 'onpaste':"return false", 'ondrag':"return false", 'ondrop':"return false"}),
        'item_quantity': forms.TextInput(attrs={'placeholder': 'Enter Quantity', 'type': 'number', 'onkeypress': 'return event.keyCode === 8 || event.charCode >= 48 && event.charCode <= 57', 'onpaste':"return false", 'ondrag':"return false", 'ondrop':"return false"}),
        'item-img': forms.FileInput()}

class CreateAccount(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']
        widgets={
        'first_name': forms.TextInput(attrs={'placeholder': 'First name','class':'w-75', 'autofocus':'true'}),
        'last_name': forms.TextInput(attrs={'placeholder': 'Last name','class':'w-75'}),
        'username': forms.TextInput(attrs={'placeholder': 'Enter username', 'class': 'mb-2', 'autocomplete':'off'}),
        'email': forms.TextInput(attrs={'placeholder': 'Email', 'class': 'mb-2', 'type': 'email', 'autocomplete':'off'}),

        }
