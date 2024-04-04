from django.db import models

from order_management.models import Order

# Create your models here.
class KitchenDisplay(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    is_prepared = models.BooleanField(default=False)