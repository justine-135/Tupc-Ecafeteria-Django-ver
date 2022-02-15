from django.db import models
from django.db.models.fields import CharField,IntegerField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import AbstractUser


class Menus(models.Model):
    FOOD_CATEGORY = (
        ('breakfast','Breakfast'),
        ('lunchmeal', 'Lunchmeal'),
        ('drinks','Beverage and Drinks'), 
        ('addons','Add-ons'),   
    )
    item_categories = CharField(max_length=20, choices=FOOD_CATEGORY, default='breakfast', blank=False)
    item_name = CharField(max_length=30, verbose_name="item_name", blank=False)
    item_quantity = IntegerField(verbose_name="item_quantity", blank=False)
    item_price = IntegerField(verbose_name="item_price", blank=False)
    item_img = ImageField(max_length=100, verbose_name="item_img", blank=False)

    def __str__(self):
        return self.item_name

class Orders(models.Model):
    time = CharField(max_length=100, verbose_name='time', blank=False)
    item = CharField(max_length=3000, verbose_name="item", blank=False)
    total_purchase = CharField(max_length=5, verbose_name="total_purchase", blank=False)
    item_status = CharField(max_length=30, verbose_name="item_status", blank=False)

class CustomUser(AbstractUser):
    menu_create = models.BooleanField(default=False)
    inventory_create = models.BooleanField(default=False)
    inventory_update = models.BooleanField(default=False)
    inventory_delete = models.BooleanField(default=False)
    orders_update = models.BooleanField(default=False)
    orders_delete = models.BooleanField(default=False)
    admins_create = models.BooleanField(default=False)
    admins_update = models.BooleanField(default=False)


