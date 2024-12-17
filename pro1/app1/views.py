from django.shortcuts import render
from rest_framework import viewsets
from . models import Employee,Leave
from . serializers import EmpSerializer,LeaveSerializer
# Create your views here.

class EmployeeViewset(viewsets.ModelViewSet):
    serializer_class=EmpSerializer
    queryset=Employee.objects.all()

class LeaveViewset(viewsets.ModelViewSet):
    serializer_class=LeaveSerializer
    queryset=Leave.objects.all()