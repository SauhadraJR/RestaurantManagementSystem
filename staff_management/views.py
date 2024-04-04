from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Employee, Shift, TimeOffRequest, WorkedHours
from ..serializers import EmployeeSerializer, ShiftSerializer, TimeOffRequestSerializer, WorkedHoursSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

class TimeOffRequestViewSet(viewsets.ModelViewSet):
    queryset = TimeOffRequest.objects.all()
    serializer_class = TimeOffRequestSerializer

class WorkedHoursViewSet(viewsets.ModelViewSet):
    queryset = WorkedHours.objects.all()
    serializer_class = WorkedHoursSerializer
