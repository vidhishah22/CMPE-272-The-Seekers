from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from LMS.models import Employee, LeaveBalance
from LMS.models import EmpLeaveRequest
from LMS.models import EmpMgrDept
import time
from django.http import JsonResponse
from django import forms


import logging
import random
from django.conf import settings
fmt = getattr(settings, 'LOG_FORMAT', None)
lvl = getattr(settings, 'LOG_LEVEL', logging.INFO)
logging.basicConfig(format=fmt, level=lvl)
logging.debug("Logging started on %s for %s" % (logging.root.name, logging.getLevelName(lvl)))
from django.core.mail import send_mail

def index(request):
    return render(request, 'LMS/base.html')

def profile(request):
    employee_list = Employee.objects.get(Email_Address='sitharakmurthy@gmail.com')
    return render(request, 'LMS/profile.html', {'employees': employee_list})

def Home(request):
    employee_list = Employee.objects.get(Email_Address='sitharakmurthy@gmail.com')
    return render(request, 'LMS/Home.html', {'employees': employee_list})

def ApplyForLeave(request):
    if request.method == "GET":
        try:
            leave_balance = LeaveBalance.objects.get(Emp_No_LeaveBal='10001', Leave_Type=request.GET['LeaveType'])
        except:
            leave_balance = LeaveBalance()
            leave_balance.Available_Days = 0

        return render(request, 'LMS/ApplyForLeave.html', {'leave_balance': leave_balance})

    else:
        employee = Employee.objects.get(Email_Address='sitharakmurthy@gmail.com')
        empMgrDept = EmpMgrDept.objects.get(Emp_No_EmpMgrDept_id = employee)
        manager = Employee.objects.get(Emp_No = empMgrDept.Manager_Emp_ID_id)

        empleaverequest = EmpLeaveRequest(Emp_ID_id = employee,Emp_FullName = empMgrDept.Emp_FullName,Leave_Type = request.POST['leaveOption'],Manager_Emp_No_id = manager,Manager_FullName = empMgrDept.Manager_FullName,Begin_Date = request.POST['BeginDate'],End_Date = request.POST['EndDate'],Requested_Days = request.POST['Days'],Leave_Status = "Pending",Emp_Comments = request.POST['Reason'])
        empleaverequest.save()
        employeeFullName = empleaverequest.Emp_FullName
        send_mail('Leave approval request for ' + employeeFullName , 'Please access leave portal to approve leave request for '+ employeeFullName+ '.\nRequest Type: '+ request.POST['leaveOption'] + "\nFrom: "+ request.POST['BeginDate']+ " \nTo:"+request.POST['EndDate'], employee.Email_Address, [empMgrDept.Manager_Email_Address], fail_silently=False)

        type = []
        beginDate = []
        endDate = []
        days = []
        status = []
        for e in EmpLeaveRequest.objects.filter(Emp_ID = "10001"):
            type.append(e.Leave_Type)
            beginDate.append(e.Begin_Date.strftime("%Y-%m-%d"))
            endDate.append(e.End_Date.strftime("%Y-%m-%d"))
            days.append(e.Requested_Days)
            status.append(e.Leave_Status)

        return render(request, 'LMS/ApplyForLeave.html', {'employees': request, 'type': type, 'beginDate': beginDate, 'endDate': endDate, 'days': days, 'status': status})

def ApproveLeave(request):
    employee_list = Employee.objects.get(Email_Address='vidhishah22@gmail.com')
    name = []
    type = []
    beginDate = []
    endDate = []
    days = []
    for e in EmpLeaveRequest.objects.filter(Manager_Emp_No = employee_list):
        name.append(e.Emp_FullName)
        type.append(e.Leave_Type)
        beginDate.append(e.Begin_Date.strftime("%Y-%m-%d"))
        endDate.append(e.End_Date.strftime("%Y-%m-%d"))
        days.append(e.Requested_Days)

    return render(request, 'LMS/ApproveLeave.html', {'employees': employee_list,'type': type, 'beginDate': beginDate, 'endDate': endDate, 'days': days, 'name': name})

#def EditEmployee1(request):
    #employee_list = Employee.objects.get(Email_Address='ac.orci@seekers.ai')
    #return render(request, 'LMS/EditEmployee.html', {'employees': employee_list})

#def EditEmployee(request):
   # if request.method == "POST":
        #if forms.is_valid():
            #if 'Email' in request.POST:
            #form = Employee(request.POST)
               # employee = Employee(Email_Address=request.POST['Email'],First_Name = request.POST['FName'], Middle_Name = request.POST['MName'],
                       # Last_Name = request.POST['LName'], Birth_Date= request.POST['DOB'], Gender = "F", Street_Address=request.POST['StreetAddress'],
                       # Address2=request.POST['Address2'], City=request.POST['City'], State=request.POST['State'],Postal_Code=request.POST['Zip'],Country=request.POST['Country'],
                       # Mobile_Number=request.POST['PhoneNo'], Hire_Date="2002-01-15", Designation="Employee", Nationality= "IN", Worktype="Permanent",IsActive="True", Emp_No = random.randint(1,1000000))


                #form.save()
               # employee.save()

           # else:
              #  employee = Employee.objects.get(Emp_No=request.POST['Emp_No'])
              #  employee.delete()

           # return render(request, 'LMS/EditEmployee.html')
        #else:
            #return HttpResponse("error")



