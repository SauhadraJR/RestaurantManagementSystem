from django.db import models

from menu_management.models import CustomizationOption, MenuItem
from table_management.models import Table

# Create your models here.

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='received')  # received, in_preparation, ready_for_delivery

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    customization_options = models.ManyToManyField(CustomizationOption)