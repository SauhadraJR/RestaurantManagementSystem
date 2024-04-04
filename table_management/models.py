from django.db import models

# Create your models here.
class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_reserved = models.BooleanField(default=False)
    is_occupied = models.BooleanField(default=False)