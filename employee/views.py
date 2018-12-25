from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from employee.models import Employee
from employee.serializers import EmployeeSerializer


class EmployeeDefaultsMixin(object):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ListEmployee(EmployeeDefaultsMixin, ListCreateAPIView):
    pass


class DetailEmployee(EmployeeDefaultsMixin, RetrieveUpdateDestroyAPIView):

    pass
