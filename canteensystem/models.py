from django.db import models
from django.db.models.fields import CharField, DecimalField, IntegerField
from django.db.models.fields.files import ImageField


class Breakfast_table(models.Model):  # Table for Breakfast
    name = CharField(max_length=30, verbose_name="name")
    img = ImageField(max_length=100, verbose_name="img")
    quantity = IntegerField(verbose_name="quantity")
    price = DecimalField(max_digits=4, decimal_places=2, verbose_name="price")

class Lunchmeal_table(models.Model):  # Table for Lunch
    name = CharField(max_length=30, verbose_name="name")
    img = ImageField(max_length=100, verbose_name="img")
    quantity = IntegerField(verbose_name="quantity")
    price = DecimalField(max_digits=4, decimal_places=2, verbose_name="price")

class Addons_table(models.Model):  # Table for Addons
    name = CharField(max_length=30, verbose_name="name")
    img = ImageField(max_length=100, verbose_name="img")
    quantity = IntegerField(verbose_name="quantity")
    price = DecimalField(max_digits=4, decimal_places=2, verbose_name="price")

class Drinks_table(models.Model):  # Table for Drinks
    name = CharField(max_length=30, verbose_name="name")
    img = ImageField(max_length=100, verbose_name="img")
    quantity = IntegerField(verbose_name="quantity")
    price = DecimalField(max_digits=4, decimal_places=2, verbose_name="price")
