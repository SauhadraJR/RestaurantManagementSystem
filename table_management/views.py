from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Table
from ..serializers import TableSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
