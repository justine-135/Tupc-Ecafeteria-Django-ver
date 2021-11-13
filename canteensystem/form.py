from django import forms
from .models import *


class FormMenu(forms.ModelForm):
    class Meta:
        model = Breakfast_table
        fields = '__all__'
