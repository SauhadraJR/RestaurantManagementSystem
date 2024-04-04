from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    stock_level = models.IntegerField()
    expiration_date = models.DateField()