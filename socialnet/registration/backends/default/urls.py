"""
URLconf for registration and activation, using django-registration's
default backend.

If the default behavior of these views is acceptable to you, simply
use a line like this in your root URLconf to set up the default URLs
for registration::

    (r'^accounts/', include('registration.backends.default.urls')),

This will also automatically set up the views in
``django.contrib.auth`` at sensible default locations.

If you'd like to customize the behavior (e.g., by passing extra
arguments to the various views) or split up the URLs, feel free to set
up your own URL patterns for these views instead.

"""


from django.conf.urls import patterns, url, include

from registration.views import register, registration_confirm

urlpatterns = patterns('',
                       url(r'^register/$',
                           register,
                           {'backend': 'registration.backends.default.DefaultBackend'},
                           name='registration_register'),
                       url(r'^registration_confirm/$',
                           registration_confirm,
                           {'backend': 'registration.backends.default.DefaultBackend'},
                           name='registration_confirm'),
                       (r'', include('registration.auth_urls')),
                       )
