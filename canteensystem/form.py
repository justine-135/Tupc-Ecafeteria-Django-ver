from django import forms
from .models import *


class BreakfastForm(forms.ModelForm):
    class Meta:
        model = Menus
        fields = ['item_name', 'item_img', 'item_price', 'item_quantity']
        widgets = {'item_name': forms.TextInput(attrs={'placeholder': 'Enter food'}),
        'item_price': forms.TextInput(attrs={'placeholder': 'Enter Price'}),
        'item_quantity': forms.TextInput(attrs={'placeholder': 'Enter Quantity'})}