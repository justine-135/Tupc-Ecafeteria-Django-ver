from django.db import models
from django.db.models.fields import CharField, DateTimeField, IntegerField
from django.db.models.fields.files import ImageField


FOOD_CATEGORY = (
    ('breakfast','Breakfast'),
    ('lunchmeal', 'Lunchmeal'),
    ('drinks','Beverage and Drinks'), 
    ('addons','Add-ons'),
)

TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)

class Menus(models.Model):
    item_categories = CharField(max_length=20, choices=FOOD_CATEGORY, default='breakfast')
    item_name = CharField(max_length=30, verbose_name="item_name")
    item_quantity = IntegerField(verbose_name="item_quantity")
    item_price = IntegerField(verbose_name="item_price")
    item_img = ImageField(max_length=100, verbose_name="item_img", blank=True)

class Orders(models.Model):
    time = DateTimeField(verbose_name='time', blank=True)
    item = CharField(max_length=30, verbose_name="item")
    total_purchase = IntegerField(verbose_name="total_purchase")
    item_status = CharField(max_length=30, verbose_name="item_status")
    cancel_order = models.CharField(max_length=30, choices = TRUE_FALSE_CHOICES)