from django.db import models
from django.db.models.fields import CharField, DecimalField, IntegerField
from django.db.models.fields.files import ImageField


class Breakfast_table(models.Model):  # Table for Breakfast

    item_name = CharField(max_length=30, verbose_name="item_name")
    item_img = ImageField(max_length=100, verbose_name="item_img")
    item_quantity = IntegerField(verbose_name="item_quantity")
    item_price = DecimalField(max_digits=4, decimal_places=2, verbose_name="item_price")


# class Lunchmeal_table(models.Model):  # Table for Lunch
#     item_name = CharField(max_length=30, verbose_name="item_name")
#     item_img = ImageField(max_length=100, verbose_name="item_img")
#     item_quantity = IntegerField(verbose_name="item_quantity")
#     item_price = DecimalField(max_digits=4, decimal_places=2, verbose_name="item_price")


# class Addons_table(models.Model):  # Table for Addons
#     item_name = CharField(max_length=30, verbose_name="item_name")
#     item_img = ImageField(max_length=100, verbose_name="item_img")
#     item_quantity = IntegerField(verbose_name="item_quantity")
#     item_price = DecimalField(max_digits=4, decimal_places=2, verbose_name="item_price")


# class Drinks_table(models.Model):  # Table for Drinks
#     item_name = CharField(max_length=30, verbose_name="item_name")
#     item_img = ImageField(max_length=100, verbose_name="item_img")
#     item_quantity = IntegerField(verbose_name="item_quantity")
#     item_price = DecimalField(max_digits=4, decimal_places=2, verbose_name="item_price")
