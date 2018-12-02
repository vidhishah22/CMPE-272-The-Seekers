from django.http import HttpResponseRedirect


def login_required(function):
    def wrap(request, *args, **kwargs):
        if 'id_token' in request.session:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/LMS/login/')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap