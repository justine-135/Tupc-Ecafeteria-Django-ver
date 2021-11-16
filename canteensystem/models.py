from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.files import ImageField


FOOD_CATEGORY = (
    ('breakfast','Breakfast'),
    ('lunchmeal', 'Lunchmeal'),
    ('drinks','Beverage and Drinks'), 
    ('addons','Add-ons'),
)

class Menus(models.Model):
    item_categories = CharField(max_length=6, choices=FOOD_CATEGORY, default='breakfast')
    item_name = CharField(max_length=30, verbose_name="item_name")
    item_quantity = IntegerField(verbose_name="item_quantity")
    item_price = IntegerField(verbose_name="item_price")
    item_img = ImageField(max_length=100, verbose_name="item_img", blank=True)

