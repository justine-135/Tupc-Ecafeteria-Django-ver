from django.db import models
from django.db.models.fields import CharField, DecimalField, IntegerField
from django.db.models.fields.files import ImageField

# gawin mo tong FOOD_CATEGORY
# palitan mo ng 
COLOR_CHOICES = (
    ('green','GREEN'), #breakfast 'Breakfast'
    ('blue', 'BLUE'), #lunchmeal 'Lunchmeal'
    ('red','RED'), #drinks 'Beverage and Drinks'
    ('orange','ORANGE'),#addons 'Add-ons'
    ('black','BLACK'),#remove to
)

class Menus(models.Model):
    item_categories = CharField(max_length=6, choices=COLOR_CHOICES, default='green') #change morin default sa 'breakfast'
    item_name = CharField(max_length=30, verbose_name="item_name")
    item_quantity = IntegerField(verbose_name="item_quantity")
    item_price = IntegerField(verbose_name="item_price")
    item_img = ImageField(max_length=100, verbose_name="item_img", blank=True)

