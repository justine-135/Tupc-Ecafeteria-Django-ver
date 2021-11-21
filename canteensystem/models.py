from django.db import models
from django.db.models.fields import CharField, DateTimeField, IntegerField
from django.db.models.fields.files import ImageField


FOOD_CATEGORY = (
    ('breakfast','Breakfast'),
    ('lunchmeal', 'Lunchmeal'),
    ('drinks','Beverage and Drinks'), 
    ('addons','Add-ons'),
)

# TRUE_FALSE_CHOICES = (
#     (True, 'Yes'),
#     (False, 'No')
# )

class Menus(models.Model):
    item_categories = CharField(max_length=20, choices=FOOD_CATEGORY, default='breakfast', blank=False)
    item_name = CharField(max_length=30, verbose_name="item_name", blank=False)
    item_quantity = IntegerField(verbose_name="item_quantity", blank=False)
    item_price = IntegerField(verbose_name="item_price", blank=False)
    item_img = ImageField(max_length=100, verbose_name="item_img", blank=False)

class Orders(models.Model):
    time = CharField(max_length=100, verbose_name='time', blank=False)
    item = CharField(max_length=30, verbose_name="item", blank=False)
    total_purchase = CharField(max_length=5, verbose_name="total_purchase", blank=False)
    item_status = CharField(max_length=30, verbose_name="item_status", blank=False)
