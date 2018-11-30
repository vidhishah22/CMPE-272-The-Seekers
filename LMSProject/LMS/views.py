from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from LMS.models import Employee
from django.http import JsonResponse

import logging
import random
from django.conf import settings
fmt = getattr(settings, 'LOG_FORMAT', None)
lvl = getattr(settings, 'LOG_LEVEL', logging.INFO)
logging.basicConfig(format=fmt, level=lvl)
logging.debug("Logging started on %s for %s" % (logging.root.name, logging.getLevelName(lvl)))

def index(request):
    return HttpResponse("Hello, World")

def base(request):
    employee_list = Employee.objects.get(Email_Address='ac.orci@seekers.ai')
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
    employee_list = Employee.objects.get(Email_Address='ac.orci@seekers.ai')
    return render(request, 'LMS/profile.html', {'employees': employee_list})
    #return render(request, 'index.html')

def Home(request):
    employee_list = Employee.objects.get(Email_Address='ac.orci@seekers.ai')
    return render(request, 'LMS/Home.html', {'employees': employee_list})

def ApplyForLeave(request):
    employee_list = Employee.objects.get(Email_Address='ac.orci@seekers.ai')
    return render(request, 'LMS/ApplyForLeave.html', {'employees': employee_list})

def ApproveLeave(request):
    employee_list = Employee.objects.get(Email_Address='ac.orci@seekers.ai')
    return render(request, 'LMS/ApproveLeave.html', {'employees': employee_list})

def EditEmployee1(request):
    employee_list = Employee.objects.get(Email_Address='ac.orci@seekers.ai')
    return render(request, 'LMS/EditEmployee.html', {'employees': employee_list})

def EditEmployee(request):
    if request.method == "POST":
        if 'Email' in request.POST:
            employee = Employee(Email_Address=request.POST['Email'],First_Name = request.POST['FName'], Middle_Name = request.POST['MName'],
                        Last_Name = request.POST['LName'], Birth_Date= request.POST['DOB'], Gender = "F", Street_Address=request.POST['StreetAddress'],
                        Address2=request.POST['Address2'], City=request.POST['City'], State=request.POST['State'],Postal_Code=request.POST['Zip'],Country=request.POST['Country'],
                        Mobile_Number=request.POST['PhoneNo'],
                        Hire_Date="2002-01-15", End_Date="2004-01-15", Designation="Employee", Nationality= "IN",
                        Worktype="Permanent",IsActive="True", Emp_No = random.randint(1,1000000))
            employee.save()
        else:
            employee = Employee.objects.get(Emp_No=request.POST['Emp_No'])
            employee.delete()

    return render(request, 'LMS/EditEmployee.html')



