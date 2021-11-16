from django.db import models
from django.db.models.fields import CharField, DecimalField, IntegerField
from django.db.models.fields.files import ImageField


class Menus(models.Model):  # Table for Breakfast

    item_name = CharField(max_length=30, verbose_name="item_name")
    item_img = ImageField(max_length=100, verbose_name="item_img", blank=True)
    item_quantity = IntegerField(verbose_name="item_quantity")
    item_price = IntegerField(verbose_name="item_price")
    item_categories = CharField(max_length=40, verbose_name="item_categories")