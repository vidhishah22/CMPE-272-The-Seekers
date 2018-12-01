from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from LMS.models import Employee
from LMS.models import EmpLeaveRequest
from LMS.models import EmpMgrDept

from django.http import JsonResponse
from django import forms


import logging
import random
from django.conf import settings
fmt = getattr(settings, 'LOG_FORMAT', None)
lvl = getattr(settings, 'LOG_LEVEL', logging.INFO)
logging.basicConfig(format=fmt, level=lvl)
logging.debug("Logging started on %s for %s" % (logging.root.name, logging.getLevelName(lvl)))

def index(request):
    return render(request, 'LMS/base.html')

def profile(request):
    employee_list = Employee.objects.get(Email_Address='ac.orci@seekers.ai')
    return render(request, 'LMS/profile.html', {'employees': employee_list})

def Home(request):
    employee_list = Employee.objects.get(Email_Address='ac.orci@seekers.ai')
    return render(request, 'LMS/Home.html', {'employees': employee_list})

def ApplyForLeave(request):
    employee = Employee.objects.get(Email_Address='felis.adipiscing.fringilla@seekers.ai')
    empMgrDept = EmpMgrDept.objects.get(Emp_No_EmpMgrDept = employee.Emp_No)
    manager = Employee.objects.get(Emp_No=empMgrDept.Manager_Emp_ID)
    if request.method == "POST":
        empLeaveRequest = EmpLeaveRequest(
        EmpLeave_Req_ID = 0,
        Emp_ID = employee,
        Emp_FullName = request.POST,
        Leave_Type = request.POST['option'],
        Manager_Emp_No = manager.Emp_No,
        Manager_FullName = "",
        Begin_Date = request.POST['Begin Date'],
        End_Date = request.POST['End Date'],
        Requested_Days = request.POST['Leaves Require'],
        Leave_Status = "Pending",
        Emp_Comments = request.POST['Reason/Comments'])
        empLeaveRequest.save()

    return render(request, 'LMS/ApplyForLeave.html', {'employees': employee})

def ApproveLeave(request):
    employee_list = Employee.objects.get(Email_Address='ac.orci@seekers.ai')
    return render(request, 'LMS/ApproveLeave.html', {'employees': employee_list})

#def EditEmployee1(request):
    #employee_list = Employee.objects.get(Email_Address='ac.orci@seekers.ai')
    #return render(request, 'LMS/EditEmployee.html', {'employees': employee_list})

def EditEmployee(request):
    if request.method == "POST":
        #if forms.is_valid():
            if 'Email' in request.POST:
            #form = Employee(request.POST)
                employee = Employee(Email_Address=request.POST['Email'],First_Name = request.POST['FName'], Middle_Name = request.POST['MName'],
                        Last_Name = request.POST['LName'], Birth_Date= request.POST['DOB'], Gender = "F", Street_Address=request.POST['StreetAddress'],
                        Address2=request.POST['Address2'], City=request.POST['City'], State=request.POST['State'],Postal_Code=request.POST['Zip'],Country=request.POST['Country'],
                        Mobile_Number=request.POST['PhoneNo'], Hire_Date="2002-01-15", Designation="Employee", Nationality= "IN", Worktype="Permanent",IsActive="True", Emp_No = random.randint(1,1000000))


                #form.save()
                employee.save()

            else:
                employee = Employee.objects.get(Emp_No=request.POST['Emp_No'])
                employee.delete()

            return render(request, 'LMS/EditEmployee.html')
        #else:
            #return HttpResponse("error")



