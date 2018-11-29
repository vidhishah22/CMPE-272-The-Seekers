from django.http import HttpResponse
from .models import Employee
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from LMS.models import Employee
from django.http import JsonResponse


"""def index(request):
    return HttpResponse("Hello, World")"""

def index(request):
    return render(request, 'LMS/index.html')


def profile(request):

    # Email_id = Employee.objects.filter(Email_Address__startswith='!????')
    employee_list = Employee.objects.get(Emp_No=10001)
    return render(request, 'LMS/profile.html', {'employees': employee_list})
    #return render(request, 'index.html')


@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.get(provider="auth0")
    userdata = {
        #'user_id': JsonResponse(Employee.objects.raw("select First_Name from Employee where Emp_No=1 "),safe=False),
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture']
    }

    return render(request, 'dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })