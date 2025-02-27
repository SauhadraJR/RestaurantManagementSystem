from django.shortcuts import render

from rest_framework import viewsets
from .models import User
from ..serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
