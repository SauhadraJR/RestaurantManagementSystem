from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Ingredient
from ..serializers import IngredientSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
