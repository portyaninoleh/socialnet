from django.shortcuts import redirect


def login_unrequired(view_func):
    """
    Decorator for views that checks that the user is not logged in, redirecting
    to the base page.
    """
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return view_func(request, *args, **kwargs)
        return redirect('/')
    return _wrapped_view_func