from django.shortcuts import redirect

def is_client(function):
    """decorator for redirect to confirmation email, all login required classes and functions should have this"""
    def _function(request, *args, **kwargs):
        if request.user.is_authenticated and not (request.user.is_superuser or request.user.is_staff):
            return redirect('index')
        return function(request, *args, **kwargs)
    return _function
