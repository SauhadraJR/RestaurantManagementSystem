from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class CustomizationOption(models.Model):
    name = models.CharField(max_length=100)
    additional_price = models.DecimalField(max_digits=6, decimal_places=2)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)