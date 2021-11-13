from django import forms
from .models import *


class BreakfastForm(forms.ModelForm):
    class Meta:
        model = Breakfast_table
        fields = ['item_name', 'item_img', 'item_price', 'item_quantity']


# class LunchmealForm(forms.ModelForm):
#     class Meta:
#         model = Lunchmeal_table
#         fields = '__all__'


# class DrinksForm(forms.ModelForm):
#     class Meta:
#         model = Drinks_table
#         fields = '__all__'


# class AddonsForm(forms.ModelForm):
#     class Meta:
#         model = Addons_table
#         fields = '__all__'
