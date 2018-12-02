from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Employee
from django.shortcuts import render
from .decorators import login_required
from django.contrib import auth
import json
import requests
from LMS.models import Employee
import jwt
from django.http import JsonResponse


"""def index(request):
    return HttpResponse("Hello, World")"""

def index(request):
    return render(request, 'LMS/index.html')

from pprint import pprint

def profile(request):

    # Email_id = Employee.objects.filter(Email_Address__startswith='!????')
    employee_list = Employee.objects.get(Emp_No=10001)
    return render(request, 'LMS/profile.html', {'employees': employee_list})
    #return render(request, 'index.html')


def login(request):
    payload = {
        'response_type': 'code',
        'client_id': 'LCTMUEpEUe9eV_0NWzAkUvkqF6cC19aT',
        'redirect_uri': 'http://localhost:8000/LMS/complete/auth0'
    }
    response = requests.get('https://seekerslms.auth0.com/authorize', params=payload)
    return HttpResponse(response)


def auth0(request):
    payload = {
        'grant_type': 'authorization_code',
        'client_id': 'LCTMUEpEUe9eV_0NWzAkUvkqF6cC19aT',
        'client_secret': 'OfVy3Tj1iNgZ__opD2NEYym_H_XZqbZiHRPJrhkuK1wYWuygwrYhWB-zfWpu2oLo',
        'code': request.GET.get('code', ''),
        'redirect_uri': 'http://localhost:8000/LMS/test'
    }
    res = requests.post('https://seekerslms.auth0.com/oauth/token', json=payload)
    request.session.flush()
    request.session['id_token'] = res.json()['id_token'];
    # payload = jwt.decode(response['id_token'], verify=False)
    # print(payload)
    # print(res.json())
    return HttpResponseRedirect('/LMS/test')


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

    return render(request, 'LMS/dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })


@login_required
def test(request):
    token = request.session['id_token']
    userinfo = jwt.decode(token, verify=False)
    request.session.flush()
    return HttpResponse(userinfo['email'])
