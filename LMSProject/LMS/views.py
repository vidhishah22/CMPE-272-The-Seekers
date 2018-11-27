from django.http import HttpResponse
from .models import Employee
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, World")


def profile(request):

    # Email_id = Employee.objects.filter(Email_Address__startswith='!????')
    employee_list = Employee.objects.get(Emp_No=10001)
    return render(request, 'LMS/profile.html', {'employees': employee_list})