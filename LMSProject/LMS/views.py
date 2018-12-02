from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Employee
from django.shortcuts import render
from .decorators import login_required, manager, hr, employee
from django.contrib import auth
import json
import requests
from LMS.models import Employee
import jwt
from django.http import JsonResponse
from pprint import pprint
from django.conf import settings


def index(request):
    return render(request, 'LMS/index.html')

@login_required
def profile(request):
        token = request.session['id_token']
        userinfo = jwt.decode(token, verify=False)
        employee_list = Employee.objects.get(Email_Address=userinfo['email'])
        return render(request, 'LMS/profile.html', {'employees': employee_list, 'role': userinfo[settings.METADATA_NAMESPACE + 'app_metadata']['role']})


def login(request):
    payload = {
        'response_type': 'code',
        'client_id': settings.AUTH0_CLIENT_ID,
        'redirect_uri': 'http://' + settings.SERVER_URL + '/LMS/complete/auth0'
    }
    response = requests.get('https://' + settings.AUTH0_DOMAIN + '/authorize', params=payload)
    return HttpResponse(response)


def auth0(request):
    payload = {
        'grant_type': 'authorization_code',
        'client_id': settings.AUTH0_CLIENT_ID,
        'client_secret': settings.AUTH0_CLIENT_SECRET,
        'code': request.GET.get('code', ''),
        'redirect_uri': 'http://' + settings.SERVER_URL + '/LMS/profile'
    }
    res = requests.post('https://' + settings.AUTH0_DOMAIN + '/oauth/token', json=payload)
    request.session.flush()
    request.session['id_token'] = res.json()['id_token']
    return HttpResponseRedirect('/LMS/profile')


@login_required
def logout(request):
    request.session.flush()
    return render(request, 'LMS/index.html')