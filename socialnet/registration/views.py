"""
Views which allow users to create and activate accounts.

"""


from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from registration.backends import get_backend
from common.decorators import login_unrequired
from profiles.models import UserProfile

@login_unrequired
def register(request, backend, activation_url=None, form_class=None,
             disallowed_url='registration_disallowed',
             template_name='registration/registration_form.html',
             extra_context=None):
    """
    Allow a new user to register an account.

    The actual registration of the account will be delegated to the
    backend specified by the ``backend`` keyword argument (see below);
    it will be used as follows:

    1. The backend's ``registration_allowed()`` method will be called,
       passing the ``HttpRequest``, to determine whether registration
       of an account is to be allowed; if not, a redirect is issued to
       the view corresponding to the named URL pattern
       ``registration_disallowed``. To override this, see the list of
       optional arguments for this view (below).

    2. The form to use for account registration will be obtained by
       calling the backend's ``get_form_class()`` method, passing the
       ``HttpRequest``. To override this, see the list of optional
       arguments for this view (below).

    3. If valid, the form's ``cleaned_data`` will be passed (as
       keyword arguments, and along with the ``HttpRequest``) to the
       backend's ``register()`` method, which should return the new
       ``User`` object.

    4. Upon successful registration, the backend's
       ``post_registration_redirect()`` method will be called, passing
       the ``HttpRequest`` and the new ``User``, to determine the URL
       to redirect the user to. To override this, see the list of
       optional arguments for this view (below).
    
    **Required arguments**
    
    None.
    
    **Optional arguments**

    ``backend``
        The dotted Python import path to the backend class to use.

    ``disallowed_url``
        URL to redirect to if registration is not permitted for the
        current ``HttpRequest``. Must be a value which can legally be
        passed to ``django.shortcuts.redirect``. If not supplied, this
        will be whatever URL corresponds to the named URL pattern
        ``registration_disallowed``.
    
    ``form_class``
        The form class to use for registration. If not supplied, this
        will be retrieved from the registration backend.
    
    ``extra_context``
        A dictionary of variables to add to the template context. Any
        callable object in this dictionary will be called to produce
        the end result which appears in the context.

    ``success_url``
        URL to redirect to after successful registration. Must be a
        value which can legally be passed to
        ``django.shortcuts.redirect``. If not supplied, this will be
        retrieved from the registration backend.
    
    ``template_name``
        A custom template to use. If not supplied, this will default
        to ``registration/registration_form.html``.
    
    **Context:**
    
    ``form``
        The registration form.
    
    Any extra variables supplied in the ``extra_context`` argument
    (see above).
    
    **Template:**
    
    registration/registration_form.html or ``template_name`` keyword
    argument.
    
    """
    backend = get_backend(backend)
    if not backend.registration_allowed(request):
        return redirect(disallowed_url)
    if form_class is None:
        form_class = backend.get_form_class(request)

    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            activation_key = backend.send_activation_email(request, **form.cleaned_data)
            request.session['form_cleaned_data'] = form.cleaned_data
            request.session['activation_key'] = activation_key
            if activation_url is None:
                to, args, kwargs = backend.post_enter_registration_data_redirect(request)
                return redirect(to, *args, **kwargs)
            else:
                return redirect(activation_url)
    else:
        form = form_class()
    
    if extra_context is None:
        extra_context = {}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value

    return render_to_response(template_name,
                              {'form': form},
                              context_instance=context)

@login_unrequired
def registration_confirm(request, backend, success_url=None, activation_form_class=None,
             disallowed_url='registration_disallowed',
             template_name='registration/registration_activation_form.html',
             extra_context=None):
    backend = get_backend(backend)
    if not backend.registration_allowed(request):
        return redirect(disallowed_url)
    if activation_form_class is None:
        activation_form_class = backend.get_confrim_form_class(request)
    form_cleaned_data = request.session.get('form_cleaned_data')

    if request.method == 'POST':
        if backend.check_user_data(**form_cleaned_data):
            form = activation_form_class(data=request.POST, files=request.FILES,
                                         activation_key=request.session.get('activation_key'))
            if form.is_valid():
                new_user = backend.register(request, **form_cleaned_data)
                first_name = form_cleaned_data.get('first_name')
                last_name = form_cleaned_data.get('last_name')
                UserProfile.objects.create(first_name=first_name, last_name=last_name)
                if success_url is None:
                    to, args, kwargs = backend.post_registration_redirect(request, new_user)
                    return redirect(to, *args, **kwargs)
                else:
                    return redirect(success_url)
        else:
            return redirect('registration_register')

    else:
        form = activation_form_class()

    if extra_context is None:
        extra_context = {}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value

    return render_to_response(template_name,
                              {'form': form},
                              context_instance=context)