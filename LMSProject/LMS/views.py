from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from LMS.models import Employee
from django.http import JsonResponse


def index(request):
    return HttpResponse("Hello, World")

def base(request):
    employee_list = Employee.objects.get(Email_Address='pragya.gautam@sjsu.edu')
    return render(request, 'LMS/base.html', {'employees': employee_list})

def profile(request):
    #user=request.user
    #auth0user=user.social_auth.get(provider="auth0")
    userdata = {
        #'user_id': JsonResponse(Employee.objects.raw("select First_Name from Employee where Emp_No=1 "),safe=False),
        #'user_id': user.id,
        #'name': user.first_name,
        #'picture': auth0user.extra_data['picture']
    }
    #Email_id=Employee.object.filter(Email_Address_startswith=????)
    #print(auth0user.extra_data['email'])
    employee_list = Employee.objects.get(Email_Address='pragya.gautam@sjsu.edu')
    return render(request, 'LMS/profile.html', {'employees': employee_list})
    #return render(request, 'index.html')

def Home(request):
    employee_list = Employee.objects.get(Email_Address='pragya.gautam@sjsu.edu')
    return render(request, 'LMS/Home.html', {'employees': employee_list})

def ApplyForLeave(request):
    employee_list = Employee.objects.get(Email_Address='pragya.gautam@sjsu.edu')
    return render(request, 'LMS/ApplyForLeave.html', {'employees': employee_list})

def ApproveLeave(request):
    employee_list = Employee.objects.get(Email_Address='pragya.gautam@sjsu.edu')
    return render(request, 'LMS/ApproveLeave.html', {'employees': employee_list})

def EditEmployee(request):
    employee_list = Employee.objects.get(Email_Address='pragya.gautam@sjsu.edu')
    return render(request, 'LMS/EditEmployee.html', {'employees': employee_list})
