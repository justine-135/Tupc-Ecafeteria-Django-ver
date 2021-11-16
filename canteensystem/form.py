from django import forms
from .models import *


class BreakfastForm(forms.ModelForm):
    class Meta:
        model = Menus
        fields = [ 'item_categories', 'item_name', 'item_price', 'item_quantity', 'item_img',]
        widgets = {'item_name': forms.TextInput(attrs={'placeholder': 'Enter food'}),
        'item_price': forms.TextInput(attrs={'placeholder': 'Enter Price'}),
        'item_quantity': forms.TextInput(attrs={'placeholder': 'Enter Quantity'})}