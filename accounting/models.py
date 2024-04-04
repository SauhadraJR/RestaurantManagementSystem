from django.db import models

from order_management.models import Order

# Create your models here.
class Bill(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)