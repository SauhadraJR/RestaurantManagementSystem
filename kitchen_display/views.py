from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import KitchenDisplay
from ..serializers import KitchenDisplaySerializer

class KitchenDisplayViewSet(viewsets.ModelViewSet):
    queryset = KitchenDisplay.objects.all()
    serializer_class = KitchenDisplaySerializer
