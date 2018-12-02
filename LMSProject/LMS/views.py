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
    employee_list = Employee.objects.get(Email_Address='pragya.gautam.92@gmail.com')
    return render(request, 'LMS/profile.html', {'employees': employee_list})

def Home(request):
    employee_list = Employee.objects.get(Email_Address='pragya.gautam.92@gmail.com')
    return render(request, 'LMS/Home.html', {'employees': employee_list})

def ApplyForLeave(request):
    employee = Employee.objects.get(Email_Address='pragya.gautam.92@gmail.com')
    empMgrDept = EmpMgrDept.objects.get(Emp_No_EmpMgrDept_id = employee)
    manager = Employee.objects.get(Emp_No = empMgrDept.Manager_Emp_ID_id)
    if request.method == "POST":
        empleaverequest = EmpLeaveRequest(Emp_ID = employee,Emp_FullName = empMgrDept.Emp_FullName,Leave_Type = request.POST['leaveOption'],Manager_Emp_No = manager,Manager_FullName = empMgrDept.Manager_FullName,Begin_Date = request.POST['BeginDate'],End_Date = request.POST['EndDate'],Requested_Days = request.POST['Days'],Leave_Status = "Pending",Emp_Comments = request.POST['Reason'])
        empleaverequest.save()
        employeeFullName = empleaverequest.Emp_FullName
        send_mail('Leave approval request for ' + employeeFullName , 'Please access leave portal to approve leave request for '+ employeeFullName+ '.\nRequest Type: '+ request.POST['leaveOption'] + '\nReason: ' +request.POST['Reason'] +'\nFrom: ' +request.POST['BeginDate']+ '\nTo:' +request.POST['EndDate'], employee.Email_Address, [empMgrDept.Manager_Email_Address], fail_silently=False)
    leavesArray = []
    for e in EmpLeaveRequest.objects.filter(Emp_ID = employee):
        leaves = {}
        leaves['Leave_Type'] = e.Leave_Type
        leaves['Begin_Date'] = e.Begin_Date.strftime("%Y-%m-%d")
        leaves['End_Date'] = e.End_Date.strftime("%Y-%m-%d")
        leaves['Requested_Days'] = e.Requested_Days
        leaves['Leave_Status'] = e.Leave_Status
        leavesArray.append(leaves)
    return render(request, 'LMS/ApplyForLeave.html', {'employees': request, 'leavesArray': leavesArray})

def ApproveLeave(request):
    employee = Employee.objects.get(Email_Address='pragya.gautam@sjsu.edu')
    approvedLeaves = request.GET.get('approveList', '')
    declinedLeaves = request.GET.get('declineList', '')

    if(approvedLeaves!=''):
        empleaverequest = EmpLeaveRequest.objects.get(EmpLeave_Req_ID=approvedLeaves)
        empleaverequest.Leave_Status = 'Approved'
        empleaverequest.save()
        send_mail('Leave approved', 'Your Leave has been approved by '+empleaverequest.Manager_FullName+".\nFrom: "+empleaverequest.Begin_Date.strftime("%Y-%m-%d")+"\nTo: "+ empleaverequest.End_Date.strftime("%Y-%m-%d"), employee.Email_Address, [employee.Email_Address],fail_silently=False)
    if(declinedLeaves!=''):
        empleaverequest = EmpLeaveRequest.objects.get(EmpLeave_Req_ID=declinedLeaves)
        empleaverequest.Leave_Status = 'Declined'
        empleaverequest.save()
        send_mail('Leave declined', 'Your Leave has been declined by '+empleaverequest.Manager_FullName+".\nFrom: "+empleaverequest.Begin_Date.strftime("%Y-%m-%d")+"\nTo: "+ empleaverequest.End_Date.strftime("%Y-%m-%d"), employee.Email_Address, [employee.Email_Address],fail_silently=False)

    leavesArray2 = []
    for e in EmpLeaveRequest.objects.filter(Manager_Emp_No = employee):
        leaves2 = {}
        leaves2['EmpLeave_Req_ID'] = e.EmpLeave_Req_ID
        leaves2['Emp_FullName'] = e.Emp_FullName
        leaves2['Emp_Comments'] = e.Emp_Comments
        leaves2['Leave_Type'] = e.Leave_Type
        leaves2['Begin_Date'] = e.Begin_Date.strftime("%Y-%m-%d")
        leaves2['End_Date'] = e.End_Date.strftime("%Y-%m-%d")
        leaves2['Requested_Days'] = e.Requested_Days
        leavesArray2.append(leaves2)

    return render(request, 'LMS/ApproveLeave.html', {'employees': employee,'leavesArray2': leavesArray2})


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



