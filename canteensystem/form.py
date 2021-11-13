from django import forms
from .models import *


class BreakfastForm(forms.ModelForm):
    class Meta:
        model = Menus
        fields = ['item_name', 'item_img', 'item_price', 'item_quantity']

