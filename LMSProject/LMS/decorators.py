from django.http import HttpResponseRedirect
import jwt
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import PermissionDenied


def login_required(function):
    def wrap(request, *args, **kwargs):
        if 'id_token' in request.session:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/LMS/login/')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def manager(function):
    def wrap(request, *args, **kwargs):
        if 'id_token' in request.session:
            token = request.session['id_token']
            userinfo = jwt.decode(token, verify=False)
            if userinfo[settings.METADATA_NAMESPACE + 'app_metadata']['role'] == 'Manager':
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        else:
            return HttpResponseRedirect('/LMS/login/')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def employee(function):
    def wrap(request, *args, **kwargs):
        if 'id_token' in request.session:
            token = request.session['id_token']
            userinfo = jwt.decode(token, verify=False)
            if userinfo[settings.METADATA_NAMESPACE + 'app_metadata']['role'] == 'Employee':
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        else:
            return HttpResponseRedirect('/LMS/login/')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def hr(function):
    def wrap(request, *args, **kwargs):
        if 'id_token' in request.session:
            token = request.session['id_token']
            userinfo = jwt.decode(token, verify=False)
            if userinfo[settings.METADATA_NAMESPACE + 'app_metadata']['role'] == 'HR':
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        else:
            return HttpResponseRedirect('/LMS/login/')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def hr_or_manager(function):
    def wrap(request, *args, **kwargs):
        if 'id_token' in request.session:
            token = request.session['id_token']
            userinfo = jwt.decode(token, verify=False)
            if userinfo[settings.METADATA_NAMESPACE + 'app_metadata']['role'] == 'HR' or \
                    userinfo[settings.METADATA_NAMESPACE + 'app_metadata']['role'] == 'Manager':
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        else:
            return HttpResponseRedirect('/LMS/login/')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def employee_or_manager(function):
    def wrap(request, *args, **kwargs):
        if 'id_token' in request.session:
            token = request.session['id_token']
            userinfo = jwt.decode(token, verify=False)
            if userinfo[settings.METADATA_NAMESPACE + 'app_metadata']['role'] == 'Employee' or \
                    userinfo[settings.METADATA_NAMESPACE + 'app_metadata']['role'] == 'Manager':
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        else:
            return HttpResponseRedirect('/LMS/login/')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap